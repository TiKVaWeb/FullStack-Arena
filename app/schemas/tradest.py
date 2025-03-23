from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum

# Перечисление для статуса сделки
class TradeStatusEnum(str, Enum):
    received = "продан"
    awaiting_payment = "ожидает оплаты"
    canceled = "отменен"

class TradeSTCreate(BaseModel):
    trade_status_st: TradeStatusEnum = Field(
        default=TradeStatusEnum.awaiting_payment,
        examples=["ожидает оплаты"],
        description="Статус сделки",
    )
    item_id: int = Field(..., examples=[1], description="ID предмета")
    buyer_ID: Optional[str] = Field(
        None, max_length=17, examples=["12345678901234567"], description="Steam ID покупателя"
    )

    class Config:
        from_attributes = True

class TradeSTUpdate(TradeSTCreate):
    pass

class TradeSTResponse(TradeSTCreate):
    id: int = Field(..., description="ID сделки")
    date_push_trade: datetime = Field(..., description="Дата создания сделки")

    class Config:
        from_attributes = True