from aiogram import types, Dispatcher, Bot, executor
from decouple import config
import logging

token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)


Admins = [996746876, ]


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    print('Обработчик старта')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello {message.from_user.first_name}\n"
                                f"Твой Telegram ID - {message.from_user.id}\n")
    await message.answer('Hello world!')



@dp.message_handler(commands="meme")
async def meme_handler(message: types.Message):
    with open('media/images.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                            photo = photo)



@dp.message_handler()
async def echo_or_square(message: types.Message):
    text = message.text
    try:
        number = float(text)
        squared = number ** 2
        await message.answer(str(squared))
    except ValueError:
        await message.answer(text)





@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
