import sqlite3 as sq

coordinates = "0.000000, 0.000000"
class indexes:
    ed = dict()
    sh = dict()
    #и т.д.
class edges: #edges = ребра
    def __init__(self, edge_type = "sea"):
        self.edge_type = edge_type
        self.edge_id = 0
        self.ice_condition = 1
        self.length = 1
        self.incident_nodes = "*id_begin_node*_*id_end_node*"
        self.max_throughput = 1
        self.tariff = 1500
    def create(self):
        #вытаскиваем поля из таблицы с помощью select и increment counter
    def update(self):
        #обновление поля из таблицы
class ship: #ship = корабль
    def __init__(self):
        self.ship_id = -1
        self.edge_position = 1
        self.edge_id = -1
        self.port_id = 1
        self.in_port = True
        self.icebreaker_id = 1
        self.max_capacity = 1
        self.node_id = 1
        self.coordinates = coordinates
        self.cargo_type = ""
        self.caravan_condition = True

class consignment: #consignment = партия груза
    def __init__(self):
        self.cargo_id = -1
        self.size = 1
        self.node_destination_id = 1
        self.ship_immediately = True
        self.type_refer = 1
        self.id_refer = 1
        self.coordinates = coordinates
        self.contracted = True

class icebreaker: #icebreaker = ледокол
    def __init__(self):
        self.icebreaker_id = 1
        self.edge_position = 1
        self.prepare_caravan = True
        self.edge_id = 1
        self.port_id = 1
        self.node_destination_id = 1
        self.speed = 40
        self.shipsin_caravan = True

class node: #node = узел
    def __init__(self):
        self.coordinates = coordinates
        self.node_id = -1

import sqlite3 as sq

with sq.connect("Ships_Icebreakers.db") as con:
    cur = con.cursor()

    # добавь столбцы
    # id ребра (INT PRIMARY KEY autoincrement)
    # ледовая обстановка, 0 если не СМП (INT)
    cur.execute("DROP TABLE IF EXISTS edges")
    cur.execute("""CREATE TABLE IF NOT EXISTS edges(
        edge_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ice_condition INTEGER,
        edge_type TEXT,
        length INTEGER,
        incident_nodes TEXT,
        max_throughput INTEGER,
        tariff TEXT
    )""")

    # добавь столбцы
    # id корабля (INT PRIMARY KEY autoincrement)
    # положение на ребре (INT)
    # id ребра, если плыпет, id порта, если стоит (INT)
    # в порту или нет (BOOLEAN)
    # id ледокола, если находится в караване (INT)
    # максимальная вместимость (INT)
    # id узела назначения (INT)
    cur.execute("DROP TABLE IF EXISTS ship")
    cur.execute("""CREATE TABLE IF NOT EXISTS ship(
    ship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edge_position INTEGER,
    edge_id INTEGER,
    port_id INTEGER,
    in_port BOOLEAN,
    icebreaker_id INTEGER,
    max_capacity INTEGER,
    node_id INTEGER,
    coordinates INTEGER NOT NULL DEFAULT "0.000000, 0.000000",
    cargo_type TEXT,
    caravan_condition BOOLEAN
    )""")

    cur.execute("DROP TABLE IF EXISTS consignment")
    # добавь столбцы
    # id груза (INT PRIMARY KEY autoincrement)
    # объем (INT),
    # узле назвачения (INT id узла, куда необходимо доставить груз),
    # хочет ли груз отправиться немедленно (BOOLEAN),
    # тип принадлежности (INT 1 - узел, 2 - ребро, 3 - кораблю)
    # id принадлежности (INT id корабля, ребра или узла)
    # coordinates INTEGER, 0 если привязан к кораблю
    cur.execute("""CREATE TABLE IF NOT EXISTS consignment(
    cargo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    size INTEGER,
    node_destination_id INTEGER,
    ship_immediately BOOLEAN,
    type_refer INTEGER,
    id_refer INTEGER,
    coordinates INTEGER,
    contracted BOOLEAN
    )""")

    # добавь столбцы
    # id ледокола (INT PRIMARY KEY autoincrement)
    # положение на ребре (INT)
    # собирает караван (BOOLEAN)
    # id ребра, если плыпет, id порта, если стоит (INT)
    # id узела назначения (INT)
    cur.execute("DROP TABLE IF EXISTS icebreaker")
    cur.execute("""CREATE TABLE IF NOT EXISTS icebreaker(
    icebreaker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edge_position INTEGER,
    prepare_caravan BOOLEAN,
    edge_id INTEGER,
    port_id INTEGER,
    node_destination_id INTEGER,
    speed INTEGER,
    shipsin_caravan BOOLEAN
    )""")

    # добавь столбцы
    # добавь PRIMARY KEY autoincrement id каждого узла
    cur.execute("DROP TABLE IF EXISTS node")
    cur.execute("""CREATE TABLE IF NOT EXISTS node(
    node_id INTEGER PRIMARY KEY AUTOINCREMENT,
    coordinates TEXT
    )""")
    SELECT * FROM edges WHERE
    def full_info():
        cur.execute(SELECT * FROM node)#вытащить все таблицы
