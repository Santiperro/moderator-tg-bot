from pydantic import BaseModel


class ChatMemberBase(BaseModel):
    tg_user_id: int
    username: str
    full_name: str
    

class ChatMemberOut(ChatMemberBase):
    id: int
    
    class Config:
        from_attributes = True
