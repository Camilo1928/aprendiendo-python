print("*** Imprimir detalles de una persona usando kwargs  ***")

# Funcion que acepta argumentos variables en forma de llave_valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recividos: ')
    for llave, valor in kwargs.items():
        print(f"{llave}:{valor}")

# llamamos la funcion
imprimir_detalle_persona(nombre="karla", edad=30, ciudad="Mexico")
imprimir_detalle_persona(nombre="carlos", edad=28, ciudad="guadalajara", puesto="Gerente")