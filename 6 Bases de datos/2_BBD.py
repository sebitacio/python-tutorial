import sqlite3

miConexion = sqlite3.connect('GestionProductos')

miCursor = miConexion.cursor()

miCursor.execute('''
CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

Productos = [
    ("Camiseta",20,"Deportes"),
    ("Jarron",40,"Ceramica"),
    ("Camion",10,"Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",Productos)

miConexion.commit()

miConexion.close()

