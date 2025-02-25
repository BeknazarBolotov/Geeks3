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
    cursor.execute(queries.TABLE_collection_products)


async def sql_insert_registered(fullname, age, gender, date_age, email, photo):
    cursor.execute(queries.INSERT_TABLE_registered, (fullname, age, gender, date_age, email, photo))
    db.commit()

async def sql_insert_store(product_name, size, price, photo):
    cursor.execute(queries.INSERT_TABLE_store, (product_name, size, price, photo))
    db.commit()

async def sql_insert_product_detail(product_id, category, infoproduct):
    cursor.execute(queries.INSERT_TABLE_product_detail, (product_id, category, infoproduct))
    db.commit()

async def sql_insert_collection_products(product_id, collection):
    cursor.execute(queries.INSERT_TABLE_collection_products, (product_id, collection))
    db.commit()

########################################################################

def get_db_connection():
    conn = sqlite3.connect('db/db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    select * from store s
    INNER JOIN product_detail pd on s.product_id = pd.product_id
    """).fetchall()
    conn.close()
    return products


def delete_products(product_id):
    conn = get_db_connection()

    conn.execute('DELETE FROM product_detail WHERE product_id = ?', (product_id,))


    conn.commit()
    conn.close()