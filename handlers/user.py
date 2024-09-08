from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart

from loader import bot
from keyboards.keyboards import menu
from locales.translations import _
import database.requests as rq


user = Router()


@user.message(CommandStart())
async def start(message: Message):
    try:
        await rq.set_user(message.from_user.id, message.from_user.first_name)
    except Exception as e:
        print(str(e))
    finally:
        lang = await rq.get_language(message.from_user.id)
        markup = menu(lang)
        await bot.send_photo(message.chat.id, photo=FSInputFile(path="images/background.jpg"),
                             caption=_("Главная", lang),
                             reply_markup=markup)
