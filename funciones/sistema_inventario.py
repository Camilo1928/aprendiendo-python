
# inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 20.99, 'cantidad': 50},
    {'id': 1, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 1, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]


# Funcion para mostrar el inventario 
def mostrar_inventario():
    for producto in inventario:
        print(f'id: {producto.get('id')}, nombre: {producto.get('nnombre')},'
        f'precio: ${producto.get('precio')}, Cantidad:{producto.get('cantidad')}')

def agregar_producto():
    pass

def buscar_producto_por_id():
    pass

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''--- Menu ---
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
            buscar_producto_por_id
        elif opcion == 4: # salir
            print('Hasta luego!')
            break
        else:
            print('Opcion invalida, proporciona una opcion valida ')