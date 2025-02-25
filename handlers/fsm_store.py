from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import main_db

class FSM_store(StatesGroup):
    product_name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    product_id = State()
    infoproduct = State()
    collection = State()
    collection_id = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await FSM_store.product_name.set()
    await message.answer('Название модели: ')


async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text

    await FSM_store.next()
    await message.answer('Размер:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_store.next()
    await message.answer('Категория: ')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text


    await FSM_store.next()
    await message.answer('Стоимость:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text


    await FSM_store.next()
    await message.answer('Фото товара: ')



async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSM_store.next()
    await message.answer("id продукта:")

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await FSM_store.next()
    await message.answer("Информация продукта: ")

async def load_infoproduct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['infoproduct'] = message.text

        await FSM_store.next()
        await message.answer("Коллекция: ")

async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text

    await FSM_store.next()
    await message.answer("ID коллекции: ")


async def load_collection_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection_id'] = message.text

    await FSM_store.next()
    await message.answer('Верные ли данные')
    await message.answer_photo(photo=data['photo'],
                               caption=f'Модель - {data["product_name"]}\n'
                                       f'Размер - {data["size"]}\n'
                                       f'Категория - {data["category"]}\n'
                                       f'Стоимость - {data["price"]}\n'
                                       f'Фото - {data["photo"]}\n'
                                       f'id продукта - {data["product_id"]}\n'
                                       f'Информация - {data["infoproduct"]}\n'
                                       f'Коллекция - {data["collection"]}\n'
                                       f'ID коллекции - {data["collection_id"]}')

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                product_name=data['product_name'],
                size=data['size'],
                price=data['price'],
                photo=data['photo']
            )
            await main_db.sql_insert_product_detail(
                product_id=data['product_id'],
                category=data['category'],
                infoproduct=data['infoproduct']
            )
            await main_db.sql_insert_collection_products(
                product_id=data['collection_id'],
                collection=data['collection']
            )


            await message.answer('Ваши данные в базе')
            await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['Store'])
    dp.register_message_handler(load_product_name, state=FSM_store.product_name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(load_product_id, state=FSM_store.product_id)
    dp.register_message_handler(load_infoproduct, state=FSM_store.infoproduct)
    dp.register_message_handler(load_collection, state=FSM_store.collection)
    dp.register_message_handler(load_collection_id, state=FSM_store.collection_id)
    dp.register_message_handler(submit, state=FSM_store.submit)