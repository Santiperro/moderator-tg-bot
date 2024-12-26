from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

# import keyboard as kb


private_router = Router()

@private_router.message(CommandStart())
async def cmd_start(message: Message):
    # Общая информация
    await message.reply('Дарова')
    

@private_router.message(Command('help'))
async def cmd_help(message: Message):
    # Список команд
    await message.answer('Помощи не будет.')

