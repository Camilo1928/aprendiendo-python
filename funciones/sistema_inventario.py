
# inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 20.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]


# Funcion para mostrar el inventario 
def mostrar_inventario():
    for producto in inventario:
        print(f"id: {producto.get('id')}, nombre: {producto.get('nombre')},"
        f"precio: ${producto.get('precio')}, Cantidad:{producto.get('cantidad')}")

# Funcion para agrear un nuevo producto al inventario
def agregar_producto():
    # pass
    print('--- Agregar nuevo producto ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre':nombre,
                      'precio':precio, 'cantidad':cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')

# Funcion para buscar un producto por ID
def buscar_producto_por_id():
    print('--- Buscar producto por Id ---')
    id_buscar = int(input('Ingresa el id a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('\nInformacion del producto encontrado: ')
            print(f'id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
                  f'Precio: ${producto.get('precio')},'
                  f'cantidad: {producto.get('cantidad')}')
            return 
    print('\nProducto NO encontrado')
    
    

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menu ---
        1. Mostrar inventario
        2. Agregar nueva producto
        3. Buscar producto por Id
        4. Salir
        ''')
        opcion = int(input('Proporciona una opcion (1-4): '))
        # Revisamos las opciones del menu
        if opcion == 1: #Mostrar el inventario
            mostrar_inventario()
        elif opcion == 2: # Agregar nuvo producto
            agregar_producto()
        elif opcion == 3: # Buscar producto por id
            buscar_producto_por_id()
        elif opcion == 4: # salir
            print('Hasta luego!')
            break
        else:
            print('Opcion invalida, proporciona una opcion valida ')