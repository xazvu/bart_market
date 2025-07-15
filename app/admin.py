from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types

from keybord import get_callback_btns

router = Router(
    name='admin',
)
btn = get_callback_btns(
    btns={
        'Добавить товар': 'add tovar',
        'Удалить товар': 'delete tovar',
    }
)

nazad = get_callback_btns(
    btns={
        'назад': 'back',
    }
)

@router.message(Command('admin'))
async def admin(message: types.Message):
    await message.answer('Hello, admin!', reply_markup=btn)


@router.callback_query(F.data == 'add tovar')
async def add_tovar(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('Хотите добавить товар?', reply_markup=nazad)
    await call.message.delete()


@router.callback_query(F.data == 'back')
async def back(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('Привет админ', reply_markup=btn)
    await call.message.delete()