from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Filter, Command

from keyboards.keyboards import menu
from locales.translations import _
from loader import bot
import config

admin = Router()


class Admin(Filter):
    def __init__(self):
        self.admin = config.admin

    async def __call__(self, message: Message):
        return message.from_user.id == self.admin


@admin.message(Admin(), Command('admin'))
async def admin_start(message: Message):
    await message.answer('Добро пожаловать в бот, администратор!')


@admin.callback_query(F.data.startswith('order:'))
async def order(callback: CallbackQuery):
    user_id = callback.message.chat.id
    service_name = callback.data.split(':')[1]
    lang = callback.data.split(':')[2]

    order_info = (f"<b>ЗАКАЗ</b>\n\n" +
                "Информация о пользователе\n" +
                f"Id: {callback.message.chat.id}\n"
                f"Имя пользователя: {callback.message.chat.username}\n\n" +
                f"Название услуги: <b>{service_name}</b>")
    keyboard = InlineKeyboardMarkup(inline_keyboard=
        [
            [
                InlineKeyboardButton(text="Написать пользователю", url=f"tg://user?id={user_id}")
            ]
        ]
    )
    await bot.send_message(config.group, order_info, reply_markup=keyboard)

    await bot.answer_callback_query(callback_query_id=callback.id,
                                    text=_("Ваша заявка отправлена. Работник свяжется с вами в ближайшее время.", lang),
                                    show_alert=True)
    markup = menu(lang)
    await callback.message.edit_caption(caption=_("Главная", lang), reply_markup=markup)
    await callback.answer()
    