from aiogram.utils.callback_data import CallbackData

category_callback_data = CallbackData('cat', "category", )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍽️ Taomga baholar", callback_data=category_callback_data.new(category='food')),
        ],
        [
            InlineKeyboardButton(text="👨‍🍳 Ofitsiant xizmatiga baholar",
                                 callback_data=category_callback_data.new(category='waiter')),
        ],
        [
            InlineKeyboardButton(text="📝 Fikr va takliflar",
                                 callback_data=category_callback_data.new(category='comment')),
        ],
    ]
)