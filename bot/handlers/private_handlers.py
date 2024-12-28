from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage

from  keyboards.keyboards import (main_keyboard as main_kb, 
                                  create_add_bot_keyboard)
from texts.bot_messages import *
from texts.bot_buttons import *


private_router = Router()
storage = MemoryStorage()

@private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_MESSAGE, 
                        reply_markup=main_kb)
    

@private_router.message(lambda message: message.text 
                        and (message.text.lower() == 'help' 
                            or message.text.lower() == '/help'))
async def cmd_help(message: Message):
    await message.answer(HELP_MESSAGE,
                         reply_markup=main_kb)


@private_router.message(F.text == ADD_BOT_BUTTON)
async def initiate_group_selection(message: Message):
    
    bot_username = (await message.bot.me()).username
    
    add_bot_kb = create_add_bot_keyboard(bot_username)

    await message.answer(
        ADD_BOT_TIP_MESSAGE,
        reply_markup=add_bot_kb
    )
