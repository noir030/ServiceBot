import asyncio
from aiogram import Dispatcher
from loader import bot, dp

from handlers.user import user
from handlers.admin import admin
from handlers.services import services
from database.models import async_main


async def main():
    dp.include_routers(user, admin, services)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    await async_main()
    print('Starting up...')


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
