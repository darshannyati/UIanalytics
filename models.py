from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "user"
    
    id: str = Field(primary_key=True)
    rid: str = Field(index=True, unique=True)
    language: str
    platform: str
    gender: str
    city: str
    state: str
    country: str
    success: bool = Field(default=False)
    request_time: datetime = Field(default_factory=datetime.utcnow)
    success_time: Optional[datetime] = Field(default=None)