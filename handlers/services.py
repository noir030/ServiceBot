from aiogram import Router, F
from aiogram.types import CallbackQuery

from loader import bot
from keyboards.keyboards import menu, categories, items, languages, order, support, group
from locales.translations import _
import database.requests as rq

services = Router()


@services.callback_query(F.data.startswith("language:"))
async def language(callback: CallbackQuery):
    lang = callback.data.split(':')[1]
    markup = languages(lang)
    await callback.message.edit_caption(caption=_("Выберите язык", lang), reply_markup=markup)
    await callback.answer()


@services.callback_query(F.data.startswith("lang:"))
async def language(callback: CallbackQuery):
    lang = callback.data.split(':')[1]
    markup = menu(lang)
    await rq.set_language(callback.from_user.id, lang)

    await bot.answer_callback_query(
        callback_query_id=callback.id,
        text=_("Язык изменён", lang),
        show_alert=True
    )

    await callback.message.edit_caption(
        caption=_("Главная", lang),
        reply_markup=markup
    )

    await callback.answer()


@services.callback_query(F.data.startswith("categories:"))
async def catalog(callback: CallbackQuery):
    lang = callback.data.split(':')[1]
    await callback.message.edit_caption(caption=_("Выберите категорию услуг", lang), reply_markup=await categories(lang))
    await callback.answer()


@services.callback_query(F.data.startswith('category:'))
async def service_list(callback: CallbackQuery):
    category_id = int(callback.data.split(':')[1])
    lang = callback.data.split(':')[2]
    await callback.message.edit_caption(
        caption=_("Выберите услугу", lang),
        reply_markup=await items(category_id, lang)
    )
    await callback.answer()


@services.callback_query(F.data.startswith('service:'))
async def service_info(callback: CallbackQuery):
    service_id = int(callback.data.split(':')[1])
    service = await rq.get_service(service_id)
    lang = callback.data.split(':')[2]
    await callback.message.edit_caption(
        caption=f"<b>{service.name}</b>\n\n{service.description}\n\n" + _("Цена", lang) + f": {service.price} €",
        reply_markup=order(service.verbose_name, lang)
    )
    await callback.answer()


@services.callback_query(F.data.startswith("support:"))
async def assist(callback: CallbackQuery):
    lang = callback.data.split(':')[1]
    markup = support(lang)
    await callback.message.edit_caption(
        caption=_("Нажмите на кнопку ниже, чтобы связаться с администратором", lang),
        reply_markup=markup
    )
    await callback.answer()


@services.callback_query(F.data.startswith("reviews:"))
async def reviews(callback: CallbackQuery):
    lang = callback.data.split(':')[1]
    markup = group(lang)
    await callback.message.edit_caption(
        caption=_("Отзывы клиентов", lang),
        reply_markup=markup
    )
    await callback.answer()


@services.callback_query(F.data.startswith('to_main:'))
async def back(callback: CallbackQuery):
    lang = callback.data.split(':')[1]
    markup = menu(lang)
    await callback.message.edit_caption(caption=_("Главная", lang), reply_markup=markup)
    await callback.answer()


@services.callback_query(F.data.startswith('to_catalog:'))
async def back_to_catalog(callback: CallbackQuery):
    lang = callback.data.split(':')[1]
    await callback.message.edit_caption(caption=_("Выберите категорию услуг", lang), reply_markup=await categories(lang))
    await callback.answer()
