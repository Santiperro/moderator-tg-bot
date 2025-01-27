from pydantic import BaseModel


class AdminBase(BaseModel):
    tg_user_id: int
    username: str
    full_name: str
    

class AdminOut(AdminBase):
    id: int
    
    class Config:
        from_attributes = True