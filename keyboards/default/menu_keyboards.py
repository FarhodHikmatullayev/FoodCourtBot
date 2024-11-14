from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_to_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🔙 Bosh Menyu"),
        ]
    ]
)