"""print('''*** Maquina de snacks ***''')

# Definimos la lista de snacks inicial
inventario = [ 
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sadwich', 'precio': 120}
]

# Lista de productos (Vacia). Son los snackts ya comprados
producto = []

# Mostramos el inventario
def mostrar_snackts():
    print("--- Snackts Disponibles ---")
    for producto in inventario:
        print(f"id: {producto.get('id')} -> {producto.get('nombre')} - {producto.get('precio')}")

# Generamos la compra
def comprar_snack():
    id_buscar = int(input("Que snack quieres comprar (id): "))
    for producto  in inventario:
        if producto.get(id) == 'id':
            print("Snack agregado: {'id': producto.get('id'), 'nombre': producto.get('nombre'), 'precio': producto.get('precio')}")
        return
    print("Producto NO encontrado con id: {id_buscar}")
    print("Snackt NO encontrado con id:{id_buscar}")

# Ticket de venta
def mostrar_ticket():
    pass


# Programa principal
if __name__ == '__main__':
    while True:
        print('''\n Menu:
        1. Mostrar snacks
        2. Comprar snack
        3. Mostrar ticket
        4. Salir
        ''')
        opcion = int(input("\nEscoge una opcion: "))
        # Revisamos las opciones del menu
        if opcion == 1: # Mostramos el menu
            mostrar_snackts()
        elif opcion == 2: # Comprar snacks
            comprar_snack()
        elif opcion == 3: # Mostramos el ticket de la venta
            mostrar_ticket()
        elif opcion == 4: # Salir
            print("Hasta luego!, Regresa pronto!")
            break
        else:
            print("opcion invalida, selectciona otra opcion!")
"""



# Repetimos el Proceso

lista_snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Tortas', 'precio': 150}
]

# Lista de productos (vacia). Son los snackts ya comprados
productos = []

def mostrar_snacks():
    print('--- Snackts Disponibles ---')
    for snack in lista_snacks:
        print(f'id: {snack.get('id')} -> {snack.get('nombre')}'
              f' - ${snack.get('precio')}')

def buscar_snack_por_id(id_buscar):
    for snack in lista_snacks:
        if snack.get('id') == id_buscar:
            return snack
    # Si llamamos al final y no se encontro el snack regresa None
    return None

def comprar_snacks():
    id_snack = int(input("Que snack quieres comprar (Id): "))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con el id: {id_snack}')

def mostrar_ticket():
    ticket = f"\t--- Ticket de Venta ---"
    total = 0
    for producto in productos:
        ticket += f"\n\t- {producto.get('nombre')} - ${producto.get('precio')}"
        total += producto.get('precio')
    ticket += f"\n\tTOTAL -> ${total}"
    print(ticket)



if __name__ == '__main__':
    while True:
        print('''\n Menu:
        1. Mostrar snackts
        2. Comprar snackts
        3. Mostrar ticket
        4. Salir ''')
        opcion = int(input("Escoge una opcion: "))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print("Hasta pronto!")
        else:
            print("Opcio invalida! Ingresa una opcion valida")