from aiogram import types, Dispatcher
from config import bot, dp
import buttons

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello {message.from_user.first_name}!\n"
                                f"Твой Telegram ID - {message.from_user.id}\n", reply_markup=buttons.start)



async def meme_handler(message: types.Message):
    with open('media/images.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                            photo = photo)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler,commands="start")
    dp.register_message_handler(meme_handler,commands="meme")