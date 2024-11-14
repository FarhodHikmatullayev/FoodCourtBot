from aiogram.dispatcher.filters.state import StatesGroup, State


class TableState(StatesGroup):
    table_number = State()
    days = State()


class FoodState(StatesGroup):
    user_id = State()
    table_number = State()
    grade = State()


class WaiterState(StatesGroup):
    user_id = State()
    table_number = State()
    grade = State()


class CommentState(StatesGroup):
    user_id = State()
    table_number = State()
    comment = State()
