from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/start')
b3 = KeyboardButton('/description')
b4 = KeyboardButton('Random photo')
b5 = KeyboardButton('/location')
kb.add(b1, b2,).add(b3).add(b4).add(b5)


kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton('Random photo')
bp2 = KeyboardButton('Menu')
kb_photo.add(bp1, bp2)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton('❤️',
                           callback_data='like')
ib2 = InlineKeyboardButton('👎',
                           callback_data='dislike')
ib3 = InlineKeyboardButton('Next photo',
                           callback_data='next')
ib4 = InlineKeyboardButton('Main menu',
                           callback_data='main')
ikb.add(ib1, ib2).add(ib3).add(ib4)

# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# b1 = KeyboardButton(text='/help')
# b2 = KeyboardButton(text='/description')
# b3 = KeyboardButton(text='Random photo')
# b4 = KeyboardButton(text='/location')
#
# kb.add(b1, b2).add(b3).add(b4)
#
# kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
# bp1 = KeyboardButton(text='Рандом')
# bp2 = KeyboardButton(text='Главное меню')
#
# kb_photo.add(bp1, bp2)
#
# ikb = InlineKeyboardMarkup(row_width=2)
# ib1 = InlineKeyboardButton(text='❤️',
#                            callback_data='like')
# ib2 = InlineKeyboardButton(text='👎',
#                            callback_data='dislike')
# ib3 = InlineKeyboardButton(text='Следующая фотка',
#                            callback_data='next')
# ib4 = InlineKeyboardButton(text='Главное меню',
#                            callback_data='main')
#
# ikb.add(ib1, ib2).add(ib3).add(ib4)