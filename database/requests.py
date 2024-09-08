from database.models import async_session
from database.models import User, Category, Service
from sqlalchemy import select, update


async def get_user(user_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == user_id))
        return user


async def set_user(user_id: int, name: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == user_id))

        if not user:
            session.add(User(user_id=user_id, name=name, lang="ru"))
            await session.commit()


async def set_language(user_id: int, lang: str) -> None:
    async with async_session() as session:
        await session.execute(update(User).where(User.user_id == user_id).values(lang=lang))
        await session.commit()


async def get_language(user_id: int) -> str:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == user_id))
        return user.lang


async def get_categories(lang: str):
    async with async_session() as session:
        return await session.scalars(select(Category).where(Category.lang == lang))


async def get_services(category_id: int):
    async with async_session() as session:
        return await session.scalars(select(Service).where(Service.category == category_id))


async def get_service(service_id: int):
    async with async_session() as session:
        return await session.scalar(select(Service).where(Service.id == service_id))
