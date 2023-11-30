import random
import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from config import TOKEN_API
from keyboards import kb, ikb, kb_photo

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = '''
<b>/help - call command to help user, cals sheet of commands</b>
<em>/start - begin to work, activates bot</em>
<em>/description - to get description about author and what this bot can do</em>
'''
arr_photos = [
    'https://preview.redd.it/cvaww687un681.jpg?width=640&crop=smart&auto=webp&s=d46d91786feab94d8e111917d3f7fab31c3757c4',
    'https://i.pinimg.com/736x/db/09/50/db095002d27e1103bd20a1c416a51c01.jpg',
    'https://i.pinimg.com/originals/8a/e2/08/8ae208afa0762c9ab768f0e5d078a19d.jpg']

photos = dict(zip(arr_photos, ['Ghost-old', 'Ghost-old', 'Ghost-new']))
random_photos = random.choice(list(photos.keys()))

flag = False


async def on_startup(_):
    print('Bot successfully has been activated')


async def random_send(message: types.Message):
    global random_photos
    random_photos = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photos,
                         caption=photos[random_photos],
                         reply_markup=ikb)


@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Random photo!',
                         reply_markup=ReplyKeyboardRemove())
    await random_send(message)
    await message.delete()


@dp.message_handler(Text(equals='Main menu'))
async def open_kb(message: types.Message):
    await message.answer(text='Welcome to Main Menu',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Welcome to our  bot 🐝',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Hello fuckers i\'m bot'
                                                         ' that created this by Saytama_kun so send him your offences) ')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAJXamVmf8kyQ4bmZLY7XwV4zg9WrA9PAAL_DAACvYBpSk6Pdn7qzRn7MwQ')
    await message.delete()


@dp.message_handler(commands=['location'])
async def location_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=random.randint(0, 50),
                            latitude=random.randint(0, 50),)
    await message.delete()


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photos
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer('You liked')
            flag = not flag
        else:
            await callback.answer('You already liked')
    elif callback.data == 'dislike':
        await callback.answer('You didn\'t like')
    elif callback.data == 'main':
        await callback.message.answer('Welcome to main menu',
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        random_photos = random.choice(list(filter(lambda x: x!= random_photos, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photos,
                                                           type='photo',
                                                           caption=photos[random_photos]),
                                          reply_markup=ikb)
        await callback.answer()

# @dp.message_handler(commands=['menu'])
# async def menu_command(message: types.Message):
#     await bot.send_message(chat_id=message.chat.id,
#                            reply_markup=ikb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
