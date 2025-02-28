from aiogram import executor
import logging
from config import dp, bot, Admins
from db.main_db import delete_products
from handlers import (commands, echo, quiz, FSM_registration,
                     fsm_store, send_products, delete_products,
                      edit_products)
from db import main_db
import buttons

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!', reply_markup=buttons.start)
        await main_db.create_tables()

async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот выключен!')



if __name__ == '__main__':
    commands.register_handlers(dp)
    quiz.register_handlers(dp)
    FSM_registration.register_handlers_fsm(dp)
    fsm_store.register_handlers_fsm(dp)
#######################################################



    send_products.register_handlers(dp)
    delete_products.register_handlers(dp)
    edit_products.register_handlers(dp)

    ##########################
    echo.register_handlers(dp)
    ##########################



    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)