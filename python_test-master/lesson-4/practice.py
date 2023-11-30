from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
HELP_COMMANDS = '''
<b>/help- command that gave you list of commands</b>
<em>/картинка - отправка каринки  </em>
<em>/location </em>
'''


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(message.text)
    # "chat.id"-send wherever can send to chat or
    # to user it depends on where you write him
    # "from_user.id" - sends only to user

    # await bot.send_message(chat_id=message.from_user.id,
    #                        text=HELP_COMMAND, parse_mode='HTML')

    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMANDS, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['картинка'])
async def image_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://www.gry-online.pl/i/h/17/407071997.jpg')
    await message.delete()


@dp.message_handler(commands=['location'])
async def help_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=40, longitude=71)
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
