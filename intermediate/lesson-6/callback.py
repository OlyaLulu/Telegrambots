from aiogram import types, executor, Dispatcher, Bot
from config import TOKEN_API

bot =Bot(TOKEN_API)
dp = Dispatcher(bot)

def





if __name__ == "__main__":
    executor.start_polling(Dispatcher=dp,
                           skip_updates=True)