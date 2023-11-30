from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

LISTS_OF_COMMAND = """
<b>/help  - calls lists of commands</b>
<em>/give - send sticker with some sticker and text</em>
<b>ALso if you'll send sticker bot will give you sticker ID, 
then if you'll send '✅' bot will count how many of this you send</b>
"""
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot successfully has been launched')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(LISTS_OF_COMMAND, parse_mode='html')


@dp.message_handler(content_types=['sticker'])
async def send_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await message.answer("Look at this dude")
    await bot.send_sticker(message.from_user.id, sticker='CAACAgQAAxkBAAICd2VUENcFqGLOF7ZPB3zTkgMv0sbuAAJUDQAC3N9pUntbXxEUjR9cMwQ')


@dp.message_handler()
async def black_heart(message: types.Message):
    if "❤" in message.text:
        await message.reply('🖤')

#
# @dp.message_handler()
# async def checkmark_count(message: types.Message):
#     await message.answer(text=str(message.text.count('✅')))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
