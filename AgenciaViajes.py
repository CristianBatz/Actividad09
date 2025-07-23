

clientes = {}
opcion = 0
while opcion != 3:
    print("=== Agencia de viajes ===")
    print("1. Registrar clientes")
    print("2. Mostrar lista de clientes")
    print("3. salir")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        print("=== Registrar clientes ===")
        cantidad = int(input("¿Cuántos clientes desea ingresar?: "))
        for a in range(cantidad):
            print(f"\ncliente #{a + 1}")
            carnet = input("Ingrese el código del cliente: ")
            clientes[carnet] = {}
            clientes[carnet]['nombre'] = input("Ingrese el nombre del cliente: ")

            cantidad_destinos = int(input("¿Cuántos destinos desea registrar?: "))
            for b in range(cantidad_destinos):
                nombre_destino = input(f"destino {b+1} : ")

                clientes[carnet][nombre_destino] = {}

    elif opcion == 2:
        print("=== LISTADO DE CLIENTES Y DESTINOS VISITADOS ===")
        for carnet, cliente in clientes.items():
            print(f"\ncliente #{carnet}")
            nombre = cliente['nombre']