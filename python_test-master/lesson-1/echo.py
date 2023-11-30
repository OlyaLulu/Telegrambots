from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(message: types.Message):
    await message.answer(message.text.capitalize())


async def on_startup(_):
    print('Bot has been successfully started up')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


