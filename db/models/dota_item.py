import datetime
from sqlalchemy import Column, Numeric, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from db.models.base_item import BaseItem


class DotaItem(BaseItem):
    __tablename__ = 'dota_item'

    history = relationship('DotaItemHistory', backref='item', lazy='dynamic')

    def __repr__(self):
        return f"{self.id}.{self.name}"


class DotaItemHistory(Base):
    __tablename__ = 'dota_item_history'

    id = Column(Integer, primary_key=True)
    price = Column(Numeric(precision=6, scale=2), nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    item_id = Column(Integer, ForeignKey('dota_item.id'))

    def __repr__(self):
        return f"< {self.item} - {self.price} >"
