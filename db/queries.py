TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    gender TEXT,
    date_age TEXT,
    email TEXT,
    photo TEXT
    )
"""


INSERT_TABLE_registered = """
    INSERT INTO registered (fullname, age, gender, date_age, email, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""


TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    size TEXT,
    price TEXT,
    photo TEXT
    )
"""
INSERT_TABLE_store = """
    INSERT INTO store (product_name, size, price, photo)
    VALUES (?, ?, ?, ?)
"""


TABLE_product_detail = """
    CREATE TABLE IF NOT EXISTS product_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    category TEXT,
    infoproduct TEXT
    )
"""

INSERT_TABLE_product_detail = """
    INSERT INTO product_detail (product_id, category, infoproduct)
    VALUES (?, ?, ?)
"""



TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    collection TEXT
    )
"""

INSERT_TABLE_collection_products = """
    INSERT INTO collection_products (product_id, collection)
    VALUES (?, ?)
"""