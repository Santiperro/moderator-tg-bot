from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class ActionType(Enum):
    DELETE = "delete"
    BAN = "ban"
    WARNING = "warning"


class ViolationType(Enum):
    SPAM = "spam"
    BAD_WORDS = "bad_words"
    KEYWORDS = "keywords"


class ViolationBase(BaseModel):
    tg_message_id: int
    chat_id: int
    chat_member_id: int
    message_content: str
    violation_type: ViolationType
    action_type: ActionType
    processed_at: datetime


class ViolationOut(ViolationBase):
    id: int
    is_cancelled: bool
    
    class Config:
        from_attributes = True
