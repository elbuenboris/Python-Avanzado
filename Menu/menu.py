class ManejadorMenu:
    def __init__(self, db_connection):
        self.conn = db_connection

    def agregar_producto(self, producto):
        query = "INSERT INTO Menu (clave, nombre, precio) VALUES (?, ?, ?)"
        self.conn.execute(query, (producto.clave, producto.nombre, producto.precio))
        self.conn.commit()

    def eliminar_producto(self, clave):
        query = "DELETE FROM Menu WHERE clave = ?"
        self.conn.execute(query, (clave,))
        self.conn.commit()

    def actualizar_producto(self, clave, nombre, precio):
        query = "UPDATE Menu SET nombre = ?, precio = ? WHERE clave = ?"
        self.conn.execute(query, (nombre, precio, clave))
        self.conn.commit()

# Resto del código en menu.py
