from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton#, ReplyKeyboardRemove



b1 = KeyboardButton('/режим_работы')
b2 = KeyboardButton('/расположение')
b3 = KeyboardButton('/каталог')
b4 = KeyboardButton('/поделиться_номером', request_contact=True)
b5 = KeyboardButton('/выйти')



kb_url_client = InlineKeyboardMarkup(row_width=2)
urlSite = InlineKeyboardButton(text="Перейти на сайт", url='https://mail.ru/')
urlContact = InlineKeyboardButton(text="Youtube", url='https://www.youtube.com/channel/UCCLye31f_uhGnJk3Vl1dYtg')
kb_url_client.add(urlContact, urlSite)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

#kb_client.add(b1).row(b2, b3).insert(b3)
kb_client.add(b1).add(b2).insert(b3).row(b4, b5)