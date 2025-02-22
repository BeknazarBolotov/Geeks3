from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

token = config('BOT_TOKEN')

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


Admins = [996746876, ]