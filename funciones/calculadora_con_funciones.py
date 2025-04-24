print("*** Calculadora con funciones ***")



def sumar():
    numero1 = float(input("Dame el valor 1: "))
    numero2 = float(input("Dame el valor 2: "))
    print(f"El resultado de la suma es: {numero1 + numero2}")

def restar():
    numero1 = float(input("Dame el valor 1: "))
    numero2 = float(input("Dame el valor 2: "))
    print(f"El resultado de la resta es:: {numero1 - numero2}")

def multiplicar():
    numero1 = float(input("Dame el valor 1: "))
    numero2 = float(input("Dame el valor 2: "))
    print(f"El resultado de la resta es:: {numero1 * numero2}")

def dividir():
    numero1 = float(input("Dame el valor 1: "))
    numero2 = float(input("Dame el valor 2: "))
    print(f"El resultado de la resta es:: {numero1 / numero2}")


if __name__ == '__main__':
    while True:
        print('''Operaciones que puedes realizar:
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Salir
               ''')
        opcion = int(input("Escoge una opcion: "))
        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir() 
        elif opcion == 5:
            print("Hasta pronto!")
            break
        else:
            print(f"opcion {opcion} invalida, proporciona una opcion valida")


