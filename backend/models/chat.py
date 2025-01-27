from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import time


class TimeInterval(BaseModel):
    start: time
    end: time


class Schedule(BaseModel):
    Monday: Optional[list[TimeInterval]] = Field(default_factory=list)
    Tuesday: Optional[list[TimeInterval]] = Field(default_factory=list)
    Wednesday: Optional[list[TimeInterval]] = Field(default_factory=list)
    Thursday: Optional[list[TimeInterval]] = Field(default_factory=list)
    Friday: Optional[list[TimeInterval]] = Field(default_factory=list)
    Saturday: Optional[list[TimeInterval]] = Field(default_factory=list)
    Sunday: Optional[list[TimeInterval]] = Field(default_factory=list)
    

class ChatBase(BaseModel):
    tg_chat_id: int
    admin_id: int
    name: str
    
    
class ChatOut(ChatBase):
    id: int
    bot_is_active: bool
    settings: dict[str, Any] = {}
    schedule: Optional[Schedule] = Field(default_factory=Schedule)
    
    class Config:
        from_attributes = True
