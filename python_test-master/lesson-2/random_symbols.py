from aiogram import Bot, executor, Dispatcher, types
from config import TOKEN_API
import random
import string

HELP_COMMAND = '''
/help- sheets of command
/description- about bot
/start- begin to work
'''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
count = 0


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text='This bot can send random symbols of alphabet ')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Welcome to my Telegram bot')
    await message.delete()


@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global count
    await message.answer(f'COUNT:{count}')
    count += 1


@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        return await message.reply('YES')
    await message.reply('NO')


@dp.message_handler()
async def send_random_symbol(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == '__main__':
    executor.start_polling(dp)
