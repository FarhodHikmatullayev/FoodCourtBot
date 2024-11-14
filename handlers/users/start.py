from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.menu import menu_keyboard, menu_keyboard_for_admins
from loader import dp, db
from states.table_states import TableState


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    user_telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
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
        await message.answer(text="👋 Salom, Botimizga xush kelibsiz!\n"
                                  "📋 Fikr bildirish uchun quyidagi bo'limlardan birini tanlang:",
                             reply_markup=menu_keyboard_for_admins)
    else:
        await message.answer(text="👋 Salom, Botimizga xush kelibsiz!\n"
                                  "📋 Fikr bildirish uchun quyidagi bo'limlardan birini tanlang:", reply_markup=menu_keyboard)
    await TableState.table_number.set()


    # for finding out table number
    if message.get_args():
        table_number = message.get_args()
    else:
        data = await state.get_data()
        table_number = data.get('table_number')
    await state.update_data(table_number=table_number)
