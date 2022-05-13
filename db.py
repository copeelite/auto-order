import sqlite3

conn = sqlite3.connect('orders.db')


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS orders"
            " (id INTEGER PRIMARY KEY, item_name text, item_number text, "
            "item_quantity text)")
        self.conn.commit()


    def fetch(self):
        self.cur.execute("SELECT * FROM orders")
        rows = self.cur.fetchall()
        return rows


    def insert(self, item_name, item_number, item_quantity):
        self.cur.execute("INSERT INTO orders VALUES (NULL, ?, ?, ?)",
                         (item_name, item_number, item_quantity))
        self.conn.commit()


    def remove(self, id):
        self.cur.execute("DELETE FROM orders WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id_id, item_name, item_number, item_quantity):
        self.cur.execute("UPDATE orders SET item_name = ?, item_number = ?, item_quantity = ? WHERE id = ?",
                         (item_name, item_number, item_quantity, id_id))
        self.conn.commit()

    def clear_quantity(self):
        self.cur.execute("UPDATE orders SET item_quantity = 0")
        self.conn.commit()

    def show_quantity(self):
        self.cur.execute("SELECT item_quantity FROM orders")
        quantity = self.cur.fetchall()
        return quantity

    def __del__(self):
        self.conn.close()
