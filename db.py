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


        db = Database('orders.db')
        db.insert('vanilla mix', '893925', '0')
        db.insert('chocolate mix', '894343', '0')
        db.insert('sherbet', '894342', '0')
        db.insert('low fat vanilla mix', '253796', '0')
        db.insert('NSA mix', '613725', '0')
        db.insert('dry whip mix', '894245', '0')
        db.insert('sorbet', '585863', '0')
        db.insert('24% whip cream', '893926', '0')
        db.insert('reese peanut butter cups', '894512', '0')
        db.insert('heath Bar', '894511', '0')
        db.insert('3 oz green sundae cup', '581959', '0')
        db.insert('lid dome green sundae cup', '252544', '0')
        db.insert('5 oz yellow sundae cup', '581962', '0')
        db.insert('lid dome yellow sundae cup', '307174', '0')
        db.insert('8 oz purple sundae cup', '540523', '0')
        db.insert('lid dome purple sundae cup', '235330', '0')
        db.insert('lid flat purple sundae cup', '895097', '0')
        db.insert('10 oz orange sundae cup', '581963', '0')
        db.insert('12 oz red sundae cup', '581964', '0')
        db.insert('lid dome red sundae cup', '307171', '0')
        db.insert('12 oz clear cup', '606965', '0')
        db.insert('16 oz clear cup', '454837', '0')
        db.insert('24 oz clear cup', '454818', '0')
        db.insert('lid flat 12-16-24 oz', '568502', '0')
        db.insert('lid dome 16-24 oz', '299730', '0')
        db.insert('32 oz clear cup', '454836', '0')
        db.insert('lid dome 32 oz', '858588', '0')
        db.insert('lid flat 32 oz', '552848', '0')
        db.insert('9 oz clear sundae cup', '892831', '0')
        db.insert('lid flat 9 oz clear sundae cup', '229092', '0')
        db.insert('16 oz sundae bowl', '383071', '0')
        db.insert('lid flat 16 oz sundae bowl', '383102', '0')
        db.insert('cone holder flat', '894398', '0')
        db.insert('pint combo', '422979', '0')
        db.insert('quart combo', '420719', '0')
        db.insert('flying saucer cracker', '231014', '0')
        db.insert('chipster chocolate chip', '267008', '0')
        db.insert('lil oreo cookie', '279269', '0')
        db.insert('lil chocolate cookie', '297692', '0')
        db.insert('bag(single flying saucer)', '894356', '0')
        db.insert('brownie', '580336', '0')
        db.insert('pond cake', '8630', '0')
        db.insert('cookie dough', '623198', '0')
        db.insert('butter finger', '408124', '0')
        db.insert('base for small square', '333157', '0')
        db.insert('base for 8 medium rounder and square', '415485', '0')
        db.insert('base for 10 large rounder and square', '415123', '0')
        db.insert('base for small sheet', '332109', '0')
        db.insert('base for large sheet', '333724', '0')
        db.insert('base for carvel log', '333725', '0')
        db.insert('strawberry puree', '893754', '0')
        db.insert('black raspberry puree', '894259', '0')
        db.insert('strawberry', '931329', '0')
        db.insert('chocolate sprinkles', '894277', '0')
        db.insert('colored sprinkles', '894276', '0')
        db.insert('cleaner floor kit', '243640', '0')
        db.insert('chocolate chip', '621741', '0')
        db.insert('tray (flying saucer)', '427121', '0')
        db.insert('banana boat container', '886274', '0')
        db.insert('tray (lil round)', '235365', '0')
        db.insert('4-cup holder', '294842', '0')
        db.insert('box small square', '624292', '0')
        db.insert('box 8 medium rounder and square', '415121', '0')
        db.insert('box 10 large rounder and square', '415120', '0')
        db.insert('box small sheet', '330395', '0')
        db.insert('box medium sheet', '333721', '0')
        db.insert('box large sheet', '333723', '0')
        db.insert('box carvel log', '440037', '0')
        db.insert('cup cake box', '603843', '0')
        db.insert('bittersweet fudge', '894486', '0')
        db.insert('milk fudge', '262152', '0')
        db.insert('caramel', '55271', '0')
        db.insert('gummy bear', '240953', '0')
        db.insert('chocolate syrup', '533110', '0')
        db.insert('peanut butter sauce', '915760', '0')
        db.insert('brown bonnet', '327035', '0')
        db.insert('cherry bonnet', '268570', '0')
        db.insert('waffle dip', '242747', '0')
        db.insert('pineapple', '856419', '0')
        db.insert('butter scotch', '89295', '0')
        db.insert('whole red cherry', '852803', '0')
        db.insert('black cherry', '369719', '0')
        db.insert('marshmallow', '893756', '0')
        db.insert('neutral piping gel', '418580', '0')
        db.insert('simple syrup', '894323', '0')
        db.insert('malt syrup', '893757', '0')
        db.insert('chocolate crunchies', '267007', '0')
        db.insert('vanilla crunchies', '271504', '0')
        db.insert('10.25 straw', '509806', '0')
        db.insert('white taste tiny spoon', '618512', '0')
        db.insert('soda float long spoon', '943086', '0')
        db.insert('regular spoon', '77691', '0')
        db.insert('deli paper(12/10.75 yellow)', '996076', '0')
        db.insert('napkin', '437345', '0')
        db.insert('paper towel roll', '158804', '0')
        db.insert('toilet tissue', '852182', '0')
        db.insert('large bag paper #12 brown', '423463', '0')
        db.insert('small bag paper #5 brown', '543903', '0')
        db.insert('small cones', '853251', '0')
        db.insert('large cones', '853249', '0')
        db.insert('sugar cones', '547428', '0')
        db.insert('waffle cones', '547152', '0')
        db.insert('cookies&cream', '858656', '0')
        db.insert('mini M&M', '894499', '0')
        db.insert('reese pieces', '969022', '0')
        db.insert('walnut', '595849', '0')
        db.insert('peanut', '894500', '0')
        db.insert('confetti sprinkles', '894275', '0')
        db.insert('toasted coconut', '357167', '0')
        db.insert('pecan nut', '870515', '0')
        db.insert('almond nut', '870514', '0')
        db.insert('small plastic bag', '564715', '0')