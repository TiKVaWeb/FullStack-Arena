from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class DialogCreate(BaseModel):
    participants: List[int] = Field(..., examples=[[1, 2]], description="Список ID участников диалога")
    last_message_id: Optional[int] = Field(None, examples=[1], description="ID последнего сообщения")

    class Config:
        from_attributes = True

class DialogUpdate(DialogCreate):
    pass

class DialogResponse(DialogCreate):
    id: int = Field(..., description="ID диалога")
    updated_at: datetime = Field(..., description="Дата последнего обновления диалога")

    class Config:
        from_attributes = True