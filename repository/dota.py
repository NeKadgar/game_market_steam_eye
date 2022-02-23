from datetime import datetime
from sqlalchemy.orm import Session

from schemas.dota_item import DotaItemCreate, DotaItemHistory, DotaItemSteamHistory
from db.models.dota_item import DotaItem as DotaItemDB
from db.models.dota_item import DotaItemHistory as DotaItemHistoryDB


def create_item(db: Session, item: DotaItemCreate):
    db_item = DotaItemDB(**item.dict())
    if db.query(DotaItemDB).filter_by(name=db_item.name).one_or_none():
        return db_item
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_item_history(db: Session, item_history: DotaItemHistory):
    db_item_history = DotaItemHistoryDB(**item_history.dict())
    db.add(db_item_history)
    db.commit()
    db.refresh(db_item_history)
    return db_item_history


def create_item_steam_history(db: Session, item_history: DotaItemSteamHistory):
    db_item_history = DotaItemHistoryDB(**item_history.dict())
    db.add(db_item_history)
    db.commit()
    db.refresh(db_item_history)
    return db_item_history


def get_item(db: Session, pk: int):
    return db.query(DotaItemDB).filter_by(id=pk).one_or_none()


def get_item_by_name(db: Session, item_hash_name: str, date_from: datetime):
    item = db.query(DotaItemDB).filter_by(name=item_hash_name).one_or_none()
    return item


def get_all_item_names(db: Session):
    for item in db.query(DotaItemDB).all():
        yield item.name, item.id
