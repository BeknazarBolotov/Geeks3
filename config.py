from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config


token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)


Admins = [996746876, ]