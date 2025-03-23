from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserSTCreate(BaseModel):
    username: str = Field(..., max_length=25, examples=["john_doe"])
    steam_ID: str = Field(..., max_length=17, examples=["12345678901234567"])
    email: Optional[EmailStr] = Field(None, examples=["john.doe@example.com"])
    telegram: Optional[str] = Field(None, max_length=20, examples=["@johndoe"])
    trade_link: Optional[str] = Field(None, examples=["https://steamcommunity.com/tradeoffer/..."])
    rating: float = Field(default=5.00, ge=0.00, le=5.00, examples=[4.5])

    class Config:
        from_attributes = True

class UserSTUpdate(UserSTCreate):
    pass

class UserSTResponse(UserSTCreate):
    id: int = Field(..., description="ID аккаунта")
