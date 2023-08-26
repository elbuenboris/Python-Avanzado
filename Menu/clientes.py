class ManejadorClientes:
    def __init__(self, db_connection):
        self.conn = db_connection

    def agregar_cliente(self, cliente):
        query = "INSERT INTO Clientes (clave, nombre, direccion, correo, telefono) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, (cliente.clave, cliente.nombre, cliente.direccion, cliente.correo, cliente.telefono))
        self.conn.commit()

    def eliminar_cliente(self, clave):
        query = "DELETE FROM Clientes WHERE clave = ?"
        self.conn.execute(query, (clave,))
        self.conn.commit()

    def actualizar_cliente(self, clave, nombre, direccion, correo, telefono):
        query = "UPDATE Clientes SET nombre = ?, direccion = ?, correo = ?, telefono = ? WHERE clave = ?"
        self.conn.execute(query, (nombre, direccion, correo, telefono, clave))
        self.conn.commit()

# Resto del código en clientes.py
