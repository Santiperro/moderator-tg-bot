from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Add bot to group")],
        [KeyboardButton(text="Manage bots"),
        KeyboardButton(text="Help")]],
    resize_keyboard=True,
    input_field_placeholder="")