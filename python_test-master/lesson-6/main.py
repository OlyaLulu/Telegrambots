from config import TOKEN_API
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LISTS_OF_COMMAND = """
<b>/help  - calls lists of commands</b>
<em>/start - send sticker with some sticker and text</em>
<b> </b>
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="Button 1",
                           url='https://www.youtube.com/')
ib2 = InlineKeyboardButton(text="Button 2",
                           url='https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1')
ikb.add(ib1, ib2)   

async def on_startup(_):
    print('Bot successfully started')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Hello world',
                           reply_markup=ikb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)