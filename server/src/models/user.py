
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from beanie import Document

class Register(BaseModel):
    email: EmailStr
    password: str
    password_repeat: str

class Login(BaseModel):
    email: EmailStr
    password: str


class User(Document):

    email: EmailStr
    password: str
    created_at: datetime = datetime.now
    storage_used: float = Field(default=0, ge=0, lt=15)
    max_storage: float = Field(default=15, ge=0, le=15)
    is_premium: bool = Field(default=False)

    class Settings:
        schema_extra = {
            "example": {
                "email": "example@example.com",
                "password": "example_password",
                "created_at": "2022-01-01T12:00:00",
                "storage_used": 0,
                "max_storage": 15.0,
                "is_premium": True
            }
        }



