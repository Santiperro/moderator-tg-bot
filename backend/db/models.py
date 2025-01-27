from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    tg_chat_id = Column(Integer, unique=True, nullable=False)
    admin_id = Column(Integer, ForeignKey("admins.id"), nullable=False)
    name = Column(String, nullable=False)
    bot_is_active = Column(Boolean, default=True)
    settings = Column(JSON, default={})
    admin = relationship("Admin", back_populates="chats")