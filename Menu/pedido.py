class ManejadorPedidos:
    def __init__(self, db_connection):
        self.conn = db_connection

    def crear_pedido(self, numero_pedido, cliente, producto, precio):
        query = "INSERT INTO Pedido (numero, cliente, producto, precio) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (numero_pedido, cliente, producto, precio))
        self.conn.commit()

        self.generar_ticket(numero_pedido, cliente, producto, precio)

    def generar_ticket(self, numero, cliente, producto, precio):
        ticket_filename = f"ticket_{numero}.txt"
        with open(ticket_filename, "w") as ticket_file:
            ticket_file.write("Pedido:\n")
            ticket_file.write(f"Número de pedido: {numero}\n")
            ticket_file.write(f"Cliente: {cliente}\n")
            ticket_file.write(f"Producto: {producto}\n")
            ticket_file.write(f"Precio: {precio}\n")
            ticket_file.write("Gracias por su compra!")

# Resto del código en pedido.py
