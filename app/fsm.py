from aiogram.fsm.state import State, StatesGroup

class Prod(StatesGroup):
    articul = State()
    category = State()
    name = State()
    price = State()
    image = State()
    posrednik = State()
    price_for_price = State()
