from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER


group_router = Router()

@group_router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER << IS_NOT_MEMBER))
async def bot_added_to_group(event: ChatMemberUpdated):
    if event.new_chat_member.user.id == (await event.bot.me()).id:
        await event.bot.send_message(event.chat.id,"123")
