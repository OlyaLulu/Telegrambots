# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
# from config import TOKEN_API
#
# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
#
#
# async def on_startup(_):
#     print("I have been started")
#
# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# b1 = KeyboardButton(text='/help')
# b2 = KeyboardButton(text='/vote')
# kb.add(b1, b2)
#
#
# @dp.message_handler(commands=['start'])
# async def command_start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Welcome to my bot',
#                            reply_markup=kb)
#
#
# @dp.message_handler(commands=['vote'])
# async def command_vote(message: types.Message):
#     ikb = InlineKeyboardMarkup(row_width=2)
#     ib1 = InlineKeyboardButton(text='❤️',
#                                callback_data='like')
#     ib2 = InlineKeyboardButton(text='👎',
#                                callback_data='dislike')
#     ikb.add(ib1, ib2)
#
#     await bot.send_photo(chat_id=message.from_user.id,
#                            photo='https://qph.cf2.quoracdn.net/main-qimg-b07da88225faa8a560049646104381a7-lq',
#                          caption='Do you like this photo',
#                          reply_markup=ikb)
#
#
# @dp.callback_query_handler()
# async def vote_callback(callback: types.CallbackQuery):
#     if callback.data == 'like':
#         await callback.answer(text='You liked this photo')
#     await callback.answer(text='You did not liked this photo')
#
# if __name__ == '__main__':
#     executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)


from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton('/help')
kb2 = KeyboardButton('/start')
kb3 = KeyboardButton('/vote')
kb.add(kb1).insert(kb2).add(kb3)


async def on_startup(_):
    print('Bot has been successfully launched')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome to my tester',
                           reply_markup=kb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here should be th text of some explanation'
                                ' however my developer is incredibly lazy about doing anything🤦🏻‍♂️')


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton('❤️',
                               callback_data='like')
    ib2 = InlineKeyboardButton('👎',
                               callback_data='dislike')
    ikb.add(ib1, ib2)

    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/22ed1c9a-cc0a-48fd-ace1-71cdf88c6067/d309wvi-5d8438e2-9b23-438b-8eb0-1ce87b864281.png/v1/fill/w_900,h_507,q_80,strp/call_of_duty_ghost_wallpaper_by_prohad_d309wvi-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTA3IiwicGF0aCI6IlwvZlwvMjJlZDFjOWEtY2MwYS00OGZkLWFjZTEtNzFjZGY4OGM2MDY3XC9kMzA5d3ZpLTVkODQzOGUyLTliMjMtNDM4Yi04ZWIwLTFjZTg3Yjg2NDI4MS5wbmciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.xyB5TIUuo0UWgiILJZhmRl7lPBFoKDVqi2fooORByGw',
                         caption='Choose photo you like more',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def call_back_vote(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='You liked this photo')
    await callback.answer(text='You didn\'t like this photo')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)