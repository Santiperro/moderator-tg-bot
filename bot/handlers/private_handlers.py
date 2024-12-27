import json
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import keyboards.main_keyboard as main_kb
from utils.message_loader import messages_loader as bot_messages


private_router = Router()


@private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(bot_messages["start_message"], 
                        reply_markup=main_kb.main_keyboard)
    

@private_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply(bot_messages["help_message"])


@private_router.message(F.text == "Add bot to group")
async def add_bot_to_group(message: Message):
    pass
