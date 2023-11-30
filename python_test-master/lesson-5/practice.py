from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import TOKEN_API
import random

HELP_COMMAND = '''
<b> /help - lists of command </b>
<em> /start - for start to work with bot </em>
<b> /description - description of bots abilities  </b>
<em> /orange - for take photo </em>
'''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/start')
b3 = KeyboardButton('/description')
b4 = KeyboardButton('/orange')
b5 = KeyboardButton('/random')
b6 = KeyboardButton('❤️')
kb.add(b1).add(b2).insert(b3).add(b4).insert(b5).add(b6)


async def on_startup(_):
    print('Bot has been successfully activated')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to Saytama\'s bot',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here is should be some kind of description however my boss asshole🤬',
                           parse_mode='HTML')
    await message.delete()

#
# @dp.message_handler(commands=['orange'])
# async def orange_command(message: types.Message):
#     await bot.send_photo(chat_id=message.chat.id,
#                          photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWFC8WcQEyvPJU-haC62zyzANo1lNNqEIUB98qOnVFXqF-OGuPmC4n8I_OSWfAwO7OXJs&usqp=CAU')
#     await message.delete()
#


@dp.message_handler(commands=['random'])
async def random_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(1, 100),
                            longitude=random.randint(1, 100))


@dp.message_handler()
async def send_sticker(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker='CAACAgIAAxkBAAEJ0xFkwcjOLm0ePaFoHh2wjhe1fION9AAC5QADV4RsDw-TVPSsuIEPLwQ')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
