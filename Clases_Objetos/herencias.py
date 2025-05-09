print("*** Herencias ***")

class Animal:

    def comer(self):
        print("Como muchas veces al dia")

    def dormir(self):
        print("Duermo muchas horas")

class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")

# Programa principal
print("*** Ejemplo de Herencia en python ***")
print("Clase Padre, soy un Animal")
animal1 = Animal()
animal1.comer()
animal1.dormir()

print("\nClase Hija, soy un Perro")
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
    


print("\n*** Ejercicio de Herencias***")


class Empresa:

    def trabajar(self):
        print("Entrada a las 6:00 am todos los dias")

    def pedidos(self):
        print("Alistamiento de muschos pedidos pedidos")

    def calidad(self):
        print("inspectores de clidad")

    def cargar_camiones(self):
        print("cargue de camiones")

class Empleado:
        
    def auxiliar(self):
        print("Recibir tuberia y clasificarla")

print("Ejemplos de herencia, de una empresa")
print("Clase de empresa")

empresa1 = Empresa()
empresa1.trabajar()
empresa1.pedidos()
empresa1.cargar_camiones()
empresa1.calidad()


print("\nClase de Empleado")
empleado1 = Empleado()
empleado1.auxiliar()