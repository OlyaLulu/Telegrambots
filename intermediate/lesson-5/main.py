from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
number = 0

def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase', callback_data='btn_increase'), InlineKeyboardButton('decrease', callback_data='btn_decrease')],
    ])
    return ikb


@dp.message_handler(commands=['start'])
async def start_cmd(message:types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                        text= f'The current {number}',
                           reply_markup=get_inline_keyboard())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def ikb_cb_handler(callback:types.CallbackQuery) -> None:
    global number
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'The current {number}',
                                         reply_markup=get_inline_keyboard())
    elif callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(f'The current {number}',
                                         reply_markup=get_inline_keyboard())
    else:
        1/0


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)