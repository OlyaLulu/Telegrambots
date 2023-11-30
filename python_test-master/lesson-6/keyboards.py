from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Youtube',
                           url='https://www.youtube.com/')
ib2 = InlineKeyboardButton(text='Google',
                           url='https://www.google.co.uz/?hl=ru')
ikb.add(ib1).add(ib2)
# ikb.add(ib1, ib2)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton('/help')
kb2 = KeyboardButton('/links')
kb.add(kb1).add(kb2)

