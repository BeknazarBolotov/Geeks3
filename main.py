from aiogram import executor
import logging
from config import dp, bot, Admins
from handlers import commands, echo, quiz
import buttons

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!')

async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот выключен!')



if __name__ == '__main__':
    commands.register_handlers(dp)
    quiz.register_handlers(dp)
    echo.register_handlers(dp)

    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)








