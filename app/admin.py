from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from keybord import get_callback_btns
from database.orm_query import orm_add_product
from fsm import Prod

router = Router(
    name='admin',
)
btn = get_callback_btns(
    btns={
        'Добавить товар': 'add tovar',
        'Удалить товар': 'delete tovar',
    }
)


@router.message(Command('admin'))
async def admin(message: types.Message):
    await message.answer('Hello, admin!', reply_markup=btn)


@router.callback_query(F.data == 'add tovar')
async def add_tovar(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Хотите добавить товар?')
    await call.message.delete()
    await state.set_state(Prod.articul)
    await call.message.answer('Введите артикуль товара')

@router.message(Prod.articul)
async def articul(message: types.Message, state: FSMContext):
    await state.update_data(articul=message.text)
    await message.answer('Введите категорию товара')
    await state.set_state(Prod.category)

@router.message(Prod.category)
async def category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer('Введите имя товара')
    await state.set_state(Prod.name)


@router.message(Prod.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара')
    await state.set_state(Prod.price)

@router.message(Prod.price)
async def price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('ставьте изображение товара')
    await state.set_state(Prod.image)

@router.message(Prod.image)
async def image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.text)
    await message.answer('Введите выручку посрденика ')
    await state.set_state(Prod.posrednik)

@router.message(Prod.posrednik)
async def posrednik(message: types.Message, state: FSMContext):
    await state.update_data(posrednik=message.text)
    await message.answer('Введите цену для перепродажи')
    await state.set_state(Prod.price_for_price)

@router.message(Prod.price_for_price)
async def price_for_price(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(price_for_price=message.text)
    await message.answer('Товар добавлен')
    data = await state.get_data()
    await orm_add_product(session, data)
    await state.clear()

    # await orm_add_product(session, data)