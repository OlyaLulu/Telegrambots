from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = '''
<b>/help = lists of command</b>
<em>/start - beginning of work </em>
<em>/картинка - отправка картинки </em>
'''


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # await message.answer(message.text)
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='Hello')
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['картинка'])
async def image_send(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://e1.pxfuel.com/desktop-wallpaper/421/588/desktop-wallpaper-soul-of-the-legend-fighter-metal-poster-golden-naruto.jpg')
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_pont(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=40, longitude=71)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
