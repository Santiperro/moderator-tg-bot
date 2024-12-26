from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command


group_router = Router()

@group_router.message(lambda message: message.chat.type in ['group', 'supergroup'])
async def handle_group_message(message: Message):
    # Проверка сообщения
    # Применение санкций при обнаружении запрещенного сообщения
    # Добавление сообщения в БД с меткой нарушения
    pass
