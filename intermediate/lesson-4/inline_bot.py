from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

is_voted = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('❤️',  callback_data='like'), InlineKeyboardButton('👎',  callback_data='dislike')],
    [InlineKeyboardButton('Close keyboard',  callback_data='close')]
])


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://dzgamingshop.com/image/cache/catalog/product/Sniper:%20Ghost%20Warrior%202/37630904_1936558519741132_6971993052655124480_n-500x500.jpg',
                         caption='Do yoi like this kind of photo?',
                         reply_markup=ikb)





@dp.callback_query_handler(text='close')
async def ikb_close_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


@dp.callback_query_handler()
async def ikb_close_cb_handler(callback: types.CallbackQuery) -> None:
    global is_voted
    if not is_voted:
        if callback.data == 'like':
            await callback.answer(show_alert=False,
                                  text='You liked it')
            is_voted = True
        await callback.answer(show_alert=False,
                              text='You did not like it')
        is_voted = True
    await callback.answer('You already liked it',
                          show_alert=True)


    # await callback.answer(show_alert=True,
    #                       text=str(callback.data))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)