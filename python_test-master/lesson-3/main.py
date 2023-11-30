from aiogram import Bot, types, executor, Dispatcher
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot has been successfully started up')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Hi <b>welcome</b> to our bot!</em>', parse_mode='HTML')


@dp.message_handler(commands=['give'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgQAAxkBAAEJudtkteU_KOYr16O1nM4ZDiKR-qII3gACoAsAAv3iYFGE3u_w4y_1zi8E')
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + '😏')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)