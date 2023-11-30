from config import TOKEN_API
from aiogram import Bot, Dispatcher, executor, types
from keyboards import ikb, kb


LISTS_OF_COMMAND = """
<b>/help  - calls lists of commands</b>
<em>/start - send sticker with some sticker and text</em>
<b> /links - send url with google and youtube</b>
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot successfully started')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Бот запущен. Начало работы. Выберите кнопку',
                         reply_markup=kb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=LISTS_OF_COMMAND)


@dp.message_handler(commands=['links'])
async def links_command(message:types.Message):
    await message.answer(text='Выберите опцию...',
                         reply_markup=ikb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)