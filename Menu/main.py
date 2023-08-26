import sqlite3
from clientes import ManejadorClientes
from menu import ManejadorMenu
from pedido import ManejadorPedidos

def imprimir_menu():
    print("Menú:")
    print("a. Pedidos")
    print("b. Clientes")
    print("c. Menú")
    print("d. Salir")

def crear_tablas(conn):
    cursor = conn.cursor()

    # Tabla de clientes
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                    clave TEXT PRIMARY KEY,
                    nombre TEXT,
                    direccion TEXT,
                    correo TEXT,
                    telefono TEXT
                )''')

    # Tabla de menú
    cursor.execute('''CREATE TABLE IF NOT EXISTS Menu (
                    clave TEXT PRIMARY KEY,
                    nombre TEXT,
                    precio REAL
                )''')

    # Tabla de pedidos
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedido (
                    numero INTEGER PRIMARY KEY,
                    cliente TEXT,
                    producto TEXT,
                    precio REAL
                )''')

    conn.commit()

def main():
    db_connection = sqlite3.connect("proyecto.db")
    crear_tablas(db_connection)

    manejador_clientes = ManejadorClientes(db_connection)
    manejador_menu = ManejadorMenu(db_connection)
    manejador_pedidos = ManejadorPedidos(db_connection)

    numero_pedido = 1
    while True:
        imprimir_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == 'a':
            print("Gestión de pedidos")
            cliente = input("Cliente: ")
            producto = input("Producto: ")
            precio = float(input("Precio: "))
            manejador_pedidos.crear_pedido(numero_pedido, cliente, producto, precio)
            numero_pedido += 1
            print("Pedido registrado y ticket generado.")

        elif opcion == 'b':
            print("Gestión de clientes")
            # Resto de la lógica para clientes
            pass

        elif opcion == 'c':
            print("Gestión de menú")
            # Resto de la lógica para menú
            pass

        elif opcion == 'd':
            print("Saliendo del programa...")
            db_connection.close()
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
