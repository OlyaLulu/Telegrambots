from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import TOKEN_API
import random

HElP_COMMAND = '''
<b>/help - lists of command </b>
<em>/start - for start to work with bot </em>
<em>/description - description of bot abilities</em>
<em>/orange - for take photo of orange </em>
<em> /saytama - for take photo of saytama </em>
'❤️' - send sticker
<b> /random - random of location sends</b>
'''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# keyboard commands
# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# b1 = KeyboardButton('/help')
# b2 = KeyboardButton('/start')
# b3 = KeyboardButton('/description')
# b4 = KeyboardButton('/orange')
# b5 = KeyboardButton('/random')
# b6 = KeyboardButton('❤️')
# b7 = KeyboardButton('/saytama')
# # insert split the display to keyboard
# # add display one button on one line to display
# kb.add(b1).add(b2).add(b3).add(b4).insert(b5).add(b6).insert(b7)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/start')
b3 = KeyboardButton('/description')
b4 = KeyboardButton('/orange')
b5 = KeyboardButton('/random')
b6 = KeyboardButton('/saytama')
b7 = KeyboardButton('❤️')
kb.insert(b1).insert(b2).insert(b3).add(b4).insert(b5).add(b6).insert(b7)


async def on_startup(_):
    print('Bot has been successfully activated')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HElP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome to Saytama_kun\'s bot',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here is should be some kind of description however my boss asshole🤬')
    await message.delete()


@dp.message_handler(commands=['orange'])
async def orange_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                           photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWFC8WcQEyvPJU-haC62zyzANo1lNNqEIUB98qOnVFXqF-OGuPmC4n8I_OSWfAwO7OXJs&usqp=CAU' )
    await message.delete()


@dp.message_handler(commands=['saytama'])
async def saytama_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                           photo='https://pm1.aminoapps.com/6495/305efb63db0a3f2caaaafb371a641ae7f591f4d3_hq.jpg' )
    await message.delete()


@dp.message_handler(commands=['random'])
async def send_location_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(1, 100),
                            longitude=random.randint(1, 100))


@dp.message_handler(content_types=['sticker'])
async def send_sticker_command(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker='CAACAgIAAxkBAAEKxM9lVrACTf2udzXDdxCbi3XTIXpV0wACFAADr8ZRGgu7XTT4sVnxMwQ')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)