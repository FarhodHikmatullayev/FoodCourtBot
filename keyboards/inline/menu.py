from aiogram.utils.callback_data import CallbackData

menu_callback_data = CallbackData('menu', "category", )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍽️ Taomga baho berish", callback_data=menu_callback_data.new(category='food')),
        ],
        [
            InlineKeyboardButton(text="👨‍🍳 Ofitsiant xizmatini baholash",
                                 callback_data=menu_callback_data.new(category='waiter')),
        ],
        [
            InlineKeyboardButton(text="📝 Fikr va taklif bildirish",
                                 callback_data=menu_callback_data.new(category='comment')),
        ],
    ]
)

menu_keyboard_for_admins = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍽️ Taomga baho berish", callback_data=menu_callback_data.new(category='food')),
        ],
        [
            InlineKeyboardButton(text="👨‍🍳 Ofitsiant xizmatini baholash",
                                 callback_data=menu_callback_data.new(category='waiter')),
        ],
        [
            InlineKeyboardButton(text="📝 Fikr va taklif bildirish",
                                 callback_data=menu_callback_data.new(category='comment')),
        ],
        [
            InlineKeyboardButton(text="📥 Fikrlarni yuklab olish",
                                 callback_data='download')
        ],
    ]
)
