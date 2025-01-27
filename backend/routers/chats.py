from fastapi import APIRouter
from models.chat import ChatBase


router = APIRouter(prefix="/chats", tags=["chats"])


@router.post("")
async def add_chat(chat: ChatBase):

    return {"message": "Chat added", "chat": chat}
