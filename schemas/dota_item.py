from typing import List
from pydantic import BaseModel, condecimal


class DotaItemHistory(BaseModel):
    price: condecimal(max_digits=6, decimal_places=2, gt=0)
    item_id: int

    class Config:
        orm_mode = True


class DotaItem(BaseModel):
    id: int
    name: str
    history: List[DotaItemHistory]

    class Config:
        orm_mode = True
