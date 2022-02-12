from sqlalchemy.orm import Session

from schemas.dota_item import DotaItemCreate, DotaItemHistory
from db.models.dota_item import DotaItem as DotaItemDB
from db.models.dota_item import DotaItemHistory as DotaItemHistoryDB


def create_item(db: Session, item: DotaItemCreate):
    db_item = DotaItemDB(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_item_history(db: Session, item_history: DotaItemHistory, item_id: int):
    db_item_history = DotaItemHistoryDB(**item_history.dict(), item_id=item_id)
    db.add(db_item_history)
    db.commit()
    db.refresh(db_item_history)
    return db_item_history


def get_item(db: Session, pk: int):
    return db.query(DotaItemDB).filter_by(id=pk).one_or_none()
