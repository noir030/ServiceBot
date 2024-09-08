translations = {
    "en": {
        "Главная": "Main",
        "Выберите язык": "Select language",
        "Язык изменён": "Language changed",
        "Выберите категорию услуг": "Choose service category",
        "Услуги": "Services",
        "Сменить язык": "Change language",
        "Поддержка": "Support",
        "Отзывы": "Reviews",
        "Выберите услугу": "Select service",
        "Заказать": "Order",
        "На главную": "Go to main",
        "Цена": "Price",
        "Ваша заявка отправлена. Работник свяжется с вами в ближайшее время.": "Your request has been sent. A worker will contact you shortly.",
        "Нажмите на кнопку ниже, чтобы связаться с администратором": "Click the button below to contact the administrator",
        "Написать в поддержку": "Contact support",
        "Отзывы клиентов": "Customer reviews",
        "Перейти в группу с отзывами": "Go to review group"
    }
}


def _(text, lang="ru"):
    if lang == "ru":
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text
