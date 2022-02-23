from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc

from db import get_session
from db.models.dota_item import DotaItemHistory
from repository import dota
from schemas.dota_item import DotaItemInfoSchema

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.get("/{item_hash_name}")
def get_item_by_name(item_hash_name: str, date_from: Optional[datetime] = None, date_to: Optional[datetime] = None,
                     db: Session = Depends(get_session)):
    item = dota.get_item_by_name(db, item_hash_name, date_from)
    history = item.history.order_by(desc(DotaItemHistory.date))
    if date_from:
        history = history.filter(DotaItemHistory.date > date_from)
    if date_to:
        history = history.filter(DotaItemHistory.date < date_to)
    return DotaItemInfoSchema(
        id=item.id,
        name=item.name,
        history=history.all()
    )
