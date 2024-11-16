from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_keyboards import back_to_menu
from keyboards.inline.confirmation import confirm_keyboard
from keyboards.inline.mark_keyboards import marks_keyboard
from keyboards.inline.menu import menu_callback_data
from keyboards.inline.web_pages import web_pages_inline_keyboard
from loader import dp, db, bot
from states.table_states import TableState, FoodState, WaiterState


@dp.callback_query_handler(menu_callback_data.filter(category='waiter'), state=TableState.table_number)
async def send_waiter_comment(call: types.CallbackQuery, state: FSMContext):
    user_telegram_id = call.from_user.id
    full_name = call.from_user.full_name
    username = call.from_user.username
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id,
        )
        user_id = user['id']
    else:
        user_id = users[0]['id']

    await call.message.edit_text(text="⭐ Ofitsiant xizmatiga baho bering:", reply_markup=marks_keyboard)
    await WaiterState.grade.set()
    await state.update_data(
        user_id=user_id,
    )


@dp.callback_query_handler(text='yes', state=WaiterState.grade)
async def confirm_saving_waiter_comment(call: types.CallbackQuery, state: FSMContext):
    user_telegram_id = call.from_user.id
    data = await state.get_data()
    grade = data.get('grade')
    table_number = data.get('table_number')
    table_number = table_number
    user_id = data.get('user_id')
    await db.create_waiter_comment(
        user_id=user_id,
        table_number=table_number,
        grade=grade
    )
    await call.message.answer(text="✅ Baho yuborildi", reply_markup=back_to_menu)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(chat_id=user_telegram_id,
                           text="Maxsus chegirma va takliflarimiz o’tkazib yubormaslik uchun sahifalarimizni kuzatib boring! 👇",
                           reply_markup=web_pages_inline_keyboard)
    await TableState.table_number.set()


@dp.callback_query_handler(text='no', state=WaiterState.grade)
async def cancel_waiter_comment(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="❌ Bekor qilindi", reply_markup=back_to_menu)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await TableState.table_number.set()


@dp.callback_query_handler(state=WaiterState.grade)
async def get_grade_for_waiter(call: types.CallbackQuery, state: FSMContext):
    mark = call.data
    mark = int(mark)
    await state.update_data(grade=mark)
    data = await state.get_data()
    grade = data.get('grade')
    await call.message.edit_text(
        text=f"⭐ Siz qo'ygan baho: {grade}\n"
             f"❓ Yuborishni xohlaysizmi?",
        reply_markup=confirm_keyboard
    )
