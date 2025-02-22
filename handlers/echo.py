from aiogram import types, Dispatcher
from random import choice



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)


async def echo_handler(message: types.Message):
    text = message.text
    if text == "game":
        games_list = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
        chosen_game = choice(games_list)
        await message.answer(f"Игральная кость: {chosen_game}")
    else:
        try:
            number = float(text)
            squared = number ** 2
            await message.answer(str(squared))
        except ValueError:
            await message.answer(text)

