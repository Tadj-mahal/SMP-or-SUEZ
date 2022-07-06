import sqlite3 as sq

coordinates = "0.000000, 0.000000"
class edges: #edges = ребра
    def __init__(self):
        self.edge_type = "sea"
        self.length = 1
        self.incident_nodes = 1
        self.max_throughput = 1
        self.tariff = 1500

class ship: #ship = корабль
    def __init__(self):
        self.coordinates = coordinates
        self.list_cargo_type = ""
        self.cargo_weight = 28000
        self.caravan_condition = True

class consignment: #consignment = партия груза
    def __init__(self):
        self.cargo_type = "sea container 40ft"
        self.coordinates = coordinates
        self.contracted = True

class icebreaker: #icebreaker = ледокол
    def __init__(self):
        self.speed = 30
        self.transfer_fee = 1000
        self.characteristics = ""
        self.shipsin_caravan = ""

class node: #node = узел
    def __init__(self):
        self.coordinates = coordinates

with sq.connect("Ships_Icebreakers.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS edges")
    cur.execute("""CREATE TABLE IF NOT EXISTS edges(
        edge_type TEXT,
        length INTEGER,
        incident_nodes INTEGER,
        max_throughput INTEGER,
        tariff INTEGER
    )""")

    cur.execute("DROP TABLE IF EXISTS ship")
    cur.execute("""CREATE TABLE IF NOT EXISTS ship(
    coordinates TEXT NOT NULL DEFAULT "0.000000, 0.000000",
    list_cargo_type TEXT,
    cargo_weight INTEGER,
    caravan_condition BLOB
    )""")

    cur.execute("DROP TABLE IF EXISTS consignment")
    cur.execute("""CREATE TABLE IF NOT EXISTS consignment(
    cargo_type TEXT,
    coordinates TEXT,
    contracted BLOB
    )""")
    #coordinates on edge
    cur.execute("DROP TABLE IF EXISTS icebreaker")
    cur.execute("""CREATE TABLE IF NOT EXISTS icebreaker(
    speed INTEGER,
    transfer_fee INTEGER,
    characteristics TEXT,
    shipsin_caravan TEXT
    )""")

    cur.execute("DROP TABLE IF EXISTS node")
    cur.execute("""CREATE TABLE IF NOT EXISTS node(
    coordinates TEXT

    )""")
