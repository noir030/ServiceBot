from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.requests import get_categories, get_services
from locales.translations import _
import config


def languages(lang):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang:ru"),
            InlineKeyboardButton(text="🇺🇸 English", callback_data="lang:en")
        ],
        [
            InlineKeyboardButton(text="\U00002B05 Назад", callback_data=f"to_main:{lang}")
        ]
    ])
    return keyboard


def menu(lang):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="\U0001F4DA " + _("Услуги", lang), callback_data=f"categories:{lang}"),
            InlineKeyboardButton(text="\U0001F310 " + _("Сменить язык", lang), callback_data=f"language:{lang}")
        ],
        [
            InlineKeyboardButton(text="\U0000260E " + _("Поддержка", lang), callback_data=f"support:{lang}"),
            InlineKeyboardButton(text="\U00002709 " + _("Отзывы", lang), callback_data=f"reviews:{lang}")
        ]
    ])
    return keyboard


async def categories(lang: str):
    all_categories = await get_categories(lang)
    keyboard = InlineKeyboardBuilder()

    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category:{category.id}:{category.lang}"))

    keyboard.row(InlineKeyboardButton(text="\U00002B05 Назад", callback_data=f"to_main:{lang}"))
    return keyboard.adjust(1).as_markup()


async def items(category_id: int, lang):
    all_services = await get_services(category_id)
    keyboard = InlineKeyboardBuilder()

    for service in all_services:
        keyboard.add(InlineKeyboardButton(text=service.name, callback_data=f"service:{service.id}:{lang}"))

    keyboard.row(InlineKeyboardButton(text="\U00002B05 Назад", callback_data=f"to_catalog:{lang}"))
    return keyboard.adjust(1).as_markup()


def order(service_name: str, lang: str):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="\U00002705 " + _("Заказать", lang), callback_data=f"order:{service_name}:{lang}"),
        ],
        [
            InlineKeyboardButton(text="\U00002B05 " + _("На главную", lang), callback_data=f"to_main:{lang}")
        ]
    ])
    return keyboard


def support(lang: str):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=(_("Написать в поддержку", lang) + " \U0000260E"), url=f"tg://user?id={config.admin}")
        ],
        [
            InlineKeyboardButton(text="\U00002B05 Назад", callback_data=f"to_main:{lang}")
        ]
    ])
    return keyboard


def group(lang: str):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=(_("Перейти в группу с отзывами", lang) + " \U00002709"), url="")
        ],
        [
            InlineKeyboardButton(text="\U00002B05 Назад", callback_data=f"to_main:{lang}")
        ]
    ])
    return keyboard
