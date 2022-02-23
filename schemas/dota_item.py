from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, condecimal, Field, validator


class SteamDotaItemHistoryRUB(BaseModel):
    price: condecimal(max_digits=10, decimal_places=2, gt=0) = Field(alias="lowest_price")
    volume: int
    median_price: condecimal(max_digits=10, decimal_places=2, gt=0)

    @validator("price", always=True)
    def validate_price(cls, value):
        return value.split()[0].replace(",", "")


class DotaItemHistory(BaseModel):
    price: condecimal(max_digits=10, decimal_places=2, gt=0)
    volume: int
    median_price: Optional[condecimal(max_digits=10, decimal_places=2, gt=0)]
    item_id: int

    class Config:
        orm_mode = True


class DotaItemSteamHistory(BaseModel):
    price: condecimal(max_digits=10, decimal_places=2, gt=0)
    volume: int
    median_price: Optional[condecimal(max_digits=10, decimal_places=2, gt=0)]
    item_id: int
    date: datetime

    class Config:
        orm_mode = True


class DotaItemCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class DotaItem(BaseModel):
    id: int
    name: str
    history: List[DotaItemHistory]

    class Config:
        orm_mode = True


class DotaItemHistoryInfoSchema(BaseModel):
    price: condecimal(max_digits=10, decimal_places=2, gt=0)
    volume: int
    median_price: Optional[condecimal(max_digits=10, decimal_places=2, gt=0)]
    date: datetime

    class Config:
        orm_mode = True


class DotaItemInfoSchema(BaseModel):
    id: int
    name: str
    history: List[DotaItemHistoryInfoSchema]

    class Config:
        orm_mode = True
