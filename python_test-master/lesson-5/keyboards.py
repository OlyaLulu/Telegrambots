from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from config import TOKEN_API


HELP_COMMAND = '''
<b> /help - lists of command </b>
<em> /start - for start to work with bot </em>
<b> /description - description of bots abilities  </b>
<em> /photo - for take photo </em>
'''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
# kb.add(b1).add(b2).add(b3)
kb.add(b1).insert(b2).add(b3)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to bot by own of Saytama',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='<b>Our bot can send photo, administration and in the future many things</b>',
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                          photo='https://e1.pxfuel.com/desktop-wallpaper/394/122/desktop-wallpaper-one-punch-man-one.jpg')

    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)