import sqlite3

miConexion=sqlite3.connect('PrimeraBase')

miCursor=miConexion.cursor()

# Crear tabla en base de datos
# miCursor.execute('CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER,SECCION VARCHAR(20))')

# Insertar producto en la tabla --------------------
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

variosProductos = [
    ("Camiseta",10,"Deportes"),
    ("Jarron",10,"Ceramica"),
    ("Camion",10,"Jugueteria")
]

# Insertar grupo de datos------------------
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)

# Leer datos de la base de datos -----------
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

print(variosProductos)

miConexion.commit()

miConexion.close()