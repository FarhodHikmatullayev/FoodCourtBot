from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.menu import menu_keyboard, menu_keyboard_for_admins
from loader import dp, db, bot
from states.table_states import TableState


@dp.message_handler(text='🔙 Bosh Menyu', state='*')
async def go_to_menu_function(message: types.Message, state: FSMContext):
    await TableState.table_number.set()
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_telegram_id = message.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id,
        )
        user_role = user['role']
    else:
        user_role = users[0]['role']
    if user_role == 'admin':
        await message.answer(text="📋 Fikr bildirish uchun quyidagi bo'limlardan birini tanlang:",
                             reply_markup=menu_keyboard_for_admins)
    else:
        await message.answer(text="📋 Fikr bildirish uchun quyidagi bo'limlardan birini tanlang:",
                             reply_markup=menu_keyboard)
