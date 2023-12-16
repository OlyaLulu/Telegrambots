from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('❤️', callback_data='like'), InlineKeyboardButton('👎🏿', callback_data='dislike')]
])


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoH58OplPXPKK_ZnqihO9bQ4PvQn6AiCZiwA&usqp=CAU',
                         caption='Do you like photo',
                         reply_markup=ikb)


@dp. callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery):
    print(callback)
    if callback.data == 'like':
        await callback.answer('You liked it!')
    await callback.answer('You didn\'t like it',)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)