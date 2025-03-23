from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class MessageCreate(BaseModel):
    dialog_id: int = Field(..., examples=[1], description="ID диалога")
    sender_id: int = Field(..., examples=[1], description="ID отправителя")
    receiver_id: int = Field(..., examples=[2], description="ID получателя")
    content: str = Field(..., examples=["Привет!"], description="Текст сообщения")
    is_read: bool = Field(default=False, examples=[False], description="Статус прочтения")

    class Config:
        from_attributes = True

class MessageUpdate(MessageCreate):
    pass

class MessageResponse(MessageCreate):
    id: int = Field(..., description="ID сообщения")
    timestamp: datetime = Field(..., description="Время отправки сообщения")

    class Config:
        from_attributes = True