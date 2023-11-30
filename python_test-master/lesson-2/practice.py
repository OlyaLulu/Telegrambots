from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import string
import random

HELP_COMMAND = """
/help - sheets of command
/description - about bot
/start - begin to work
/count - counts how many users write count command
/random - random letters generator
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
count = 0


# Writes that bot activated on terminal
async def on_startup(_):
    print('Bot successfully has been started!')


# displays help command variable
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()


# bot ability displays
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text='This bot can send random symbols of alphabet and count how many count command did you '
                              'sent, can also say Yes if you have zero in your inputs, but now it is off')
    await message.delete()


# starts bot
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Welcome to Saytama_kun's bot")
    await message.delete()


# count how many user input command count
@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1


"""
be careful about this two conditions because now this bot can work only with one condition at one time
 and ignoring the second one
"""

# @dp.message_handler()
# async def check_zero(message: types.Message):
#     if "0" in message.text:
#         await message.answer(text="Yes")
#     else:
#         await message.reply("No")


# sends one random string
@dp.message_handler(commands=['random'])
async def send_random_symbols(message: types.Message):
    if message.text == '/random':
        await message.reply(random.choice(string.ascii_letters))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)