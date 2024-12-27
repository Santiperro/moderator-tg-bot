import json
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import keyboards.main_keyboard as main_kb
from texts.bot_messages import *


private_router = Router()


@private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_MESSAGE, 
                        reply_markup=main_kb.main_keyboard)
    

@private_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(HELP_MESSAGE)


@private_router.message(F.text == "Add bot to group")
async def add_bot_to_group(message: Message):
    pass
