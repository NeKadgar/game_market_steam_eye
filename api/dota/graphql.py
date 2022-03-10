import graphene
from sqlalchemy import desc


from db import get_session
from db.models.dota_item import DotaItemHistory
from repository import dota
from schemas.dota_item import DotaItemInfoSchema


database_session = next(get_session())


class DotaItemHistoryModel(graphene.ObjectType):
    id = graphene.ID()
    price = graphene.Decimal()
    volume = graphene.Int()
    median_price = graphene.Decimal()
    date = graphene.DateTime()


class DotaItemModel(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    history = graphene.List(DotaItemHistoryModel)


class Query(graphene.ObjectType):
    item_history_by_id = graphene.Field(DotaItemModel, item_id=graphene.Int())
    items_history_by_name = graphene.Field(graphene.List(DotaItemModel),
                                           item_names=graphene.List(of_type=graphene.String, required=True),
                                           date_from=graphene.DateTime(), date_to=graphene.DateTime())

    def resolve_item_history_by_id(root, info, item_id):
        item = dota.get_item(database_session, item_id)
        history = item.history.order_by(desc(DotaItemHistory.date))
        return DotaItemInfoSchema(
            id=item.id,
            name=item.name,
            history=history.all()
        )

    def resolve_items_history_by_name(root, info, item_names, date_from, date_to):
        output = []
        items = dota.get_items_by_name_list(database_session, item_names=item_names)
        for item in items:
            history = item.history.order_by(desc(DotaItemHistory.date))
            if date_from:
                history = history.filter(DotaItemHistory.date > date_from)
            if date_to:
                history = history.filter(DotaItemHistory.date < date_to)
            output.append(DotaItemInfoSchema(
                id=item.id,
                name=item.name,
                history=history.all()
            ))
        return output
