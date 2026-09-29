import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")

cur.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Bilal", "Islamabad"),
    (4, "Ayesha", "Karachi"),
    (5, "Usman", "Lahore"),
    (6, "Hamza", "Rawalpindi")
]

orders = [
    (1, 1, 4500),
    (2, 1, 7200),
    (3, 2, 3000),
    (4, 2, 6500),
    (5, 3, 8000),
    (6, 3, 5500),
    (7, 4, 2500),
    (8, 4, 6000),
    (9, 5, 5800),
    (10, 6, 7000)
]

cur.executemany("""
INSERT INTO customers
(customer_id, name, city)
VALUES (?, ?, ?)
""", customers)

cur.executemany("""
INSERT INTO orders
(order_id, customer_id, amount)
VALUES (?, ?, ?)
""", orders)

conn.commit()
conn.close()

print("orders.db created successfully.")
