import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite')
cursor = db.cursor()

async def create_tables():
    if db:
        print('База данных подключена')
    cursor.execute(queries.TABLE_registered)
    cursor.execute(queries.TABLE_store)
    cursor.execute(queries.TABLE_product_detail)


async def sql_insert_registered(fullname, age, gender, date_age, email, photo):
    cursor.execute(queries.INSERT_TABLE_registered, (fullname, age, gender, date_age, email, photo))
    db.commit()

async def sql_insert_store(product_name, size, price, photo):
    cursor.execute(queries.INSERT_TABLE_store, (product_name, size, price, photo))
    db.commit()

async def sql_insert_product_detail(product_id, category, infoproduct):
    cursor.execute(queries.INSERT_TABLE_product_detail, (product_id, category, infoproduct))
    db.commit()