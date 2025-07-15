from .models import Product
from sqlalchemy.ext.asyncio import AsyncSession


async def orm_add_product(session: AsyncSession, data: dict):
    obj = Product(
        articul=data["articul"],
        category=data["category"],
        name=data["name"],
        price=data["price"],
        image=data["image"],
        posrednik=data["posrednik"],
        price_for_price=data["price_for_price"],
    )
    session.add(obj)
    await session.commit()