from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class ItemSTCreate(BaseModel):
    item_steam_ID: str = Field(..., max_length=25, examples=["12345"], description="Steam ID предмета")
    price: float = Field(..., gt=0, examples=[100.0], description="Цена предмета")
    status_trade: bool = Field(default=True, examples=[True], description="Статус торговли")
    user_id: Optional[int] = Field(None, examples=[1], description="ID пользователя, владеющего предметом")

    class Config:
        from_attributes = True

class ItemSTUpdate(ItemSTCreate):
    pass

class ItemSTResponse(ItemSTCreate):
    id: int = Field(..., description="ID предмета")
    date_push_item: datetime = Field(..., description="Дата добавления предмета")

    class Config:
        from_attributes = True