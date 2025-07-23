def cantidad_destinos(cantidad, cantidad_clientes, cantidad_viajes):
    if (cantidad <= cantidad_clientes):
        return True
    else:
        cantidad_viajes = cantidad_viajes + 1
        return cantidad_viajes


def cliente_destinos_mas(clientes, lista_clientes, indice=0, cliente_mayor='', maximos_destinos=0):
    if indice >= len(lista_clientes):
        return cliente_mayor, maximos_destinos


clientes = {}
cantidad_viajes = 0
opcion = 0
while opcion != 3:
    print("=== Agencia de viajes ===")
    print("1. Registrar clientes")
    print("2. Mostrar lista de clientes")
    print("3. salir")
    try:
        opcion = int(input("Selecciona una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue

    if opcion == 1:
        cantidad_viajes = 0
        print("=== Registrar clientes ===")
        cantidad = int(input("¿Cuántos clientes desea ingresar?: "))
        cantidad_clientes = cantidad
        for a in range(cantidad):
            print(f"\ncliente #{a + 1}")
            carnet = input("Ingrese el código del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")

            clientes[carnet] = {
                'nombre': nombre,
                'destinos': {}
            }

            numero_destinos = int(input("¿Cuántos destinos desea registrar?: "))
            cantidad_destino = numero_destinos
            for b in range(numero_destinos):
                nombre_destino = input(f"Destino {b + 1}: ")
                clientes[carnet]['destinos'][nombre_destino] = {}
                cantidad_viajes = cantidad_destinos(numero_destinos, cantidad_clientes, cantidad_viajes)



    elif opcion == 2:
        print("=== LISTADO DE CLIENTES Y DESTINOS VISITADOS ===")
        for carnet, cliente in clientes.items():
            print(f"\ncliente #{carnet}")
            print(f"Nombre: {cliente['nombre']}")
            for destino, destinos in cliente['destinos'].items():
                print(f"Destinos: {destino}")

        print("=== DESTINOS VISITADOS ===")
        print(f"Total de destinos registrados entre todos los clientes: {cantidad_viajes}")

        lista_clientes = list(clientes.keys())
        if lista_clientes:
            cliente_mayor, total_destinos = cliente_destinos_mas(clientes, lista_clientes)
            print(f"Cliente con más destinos: {clientes[cliente_mayor]['nombre']} ({total_destinos} visitados)")
