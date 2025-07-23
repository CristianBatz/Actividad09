def sumar_destinos(clientes, lista_clientes, indice=0):
    if indice >= len(lista_clientes):
        return 0
    carnet = lista_clientes[indice]
    cantidad = clientes[carnet]['cantidad_destinos']
    return cantidad + sumar_destinos(clientes, lista_clientes, indice + 1)

def cliente_destinos(clientes, lista_clientes, indice=0, cliente_mayor='', maximos_destinos=0):
    if indice >= len(lista_clientes):
        return cliente_mayor, maximos_destinos
    else:
        carnet = lista_clientes[indice]
        destinos_actuales = len(clientes[carnet]['destinos'])
        if destinos_actuales > maximos_destinos:
            cliente_mayor = carnet
            maximos_destinos = destinos_actuales
        return cliente_destinos(clientes, lista_clientes, indice + 1, cliente_mayor, maximos_destinos)

clientes = {}
cantidad_viajes = 1
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
        cantidad_viajes = 1
        print("=== Registrar clientes ===")
        cantidad = int(input("¿Cuántos clientes desea ingresar?: "))
        for a in range(cantidad):
            print(f"\ncliente #{a + 1}")
            carnet = input("Ingrese el código del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")

            numero_destinos = int(input("¿Cuántos destinos desea registrar?: "))
            clientes[carnet] = {
                'nombre': nombre,
                'destinos': {},
                'cantidad_destinos': numero_destinos
            }

            for b in range(numero_destinos):
                nombre_destino = input(f"Destino {b + 1}: ")
                clientes[carnet]['destinos'][nombre_destino] = {}

    elif opcion == 2:
        print("=== LISTADO DE CLIENTES Y DESTINOS VISITADOS ===")
        for carnet, cliente in clientes.items():
            print(f"\ncliente #{carnet}")
            print(f"Nombre: {cliente['nombre']}")
            for destino, destinos in cliente['destinos'].items():
                print(f"Destino: {destino}")

        print("=== DESTINOS VISITADOS ===")
        lista_clientes = list(clientes.keys())
        total_destinos = sumar_destinos(clientes, lista_clientes)
        print(f"Total de destinos registrados entre todos los clientes: {total_destinos}")

        lista_clientes = list(clientes.keys())
        if lista_clientes:
            cliente_mayor, total_destinos = cliente_destinos(clientes, lista_clientes)
            print(f"Cliente con más destinos: {clientes[cliente_mayor]['nombre']} ({total_destinos} visitados)")
