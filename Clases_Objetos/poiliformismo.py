# poliformismo 

class Animal:
    def hacer_sonido(self):
        print("Hago un pitido")
    
class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")

class Gato(Animal):
    def hacer_sonido(self):
        print("Puedo maullar")

print("*** Ejemplo Poliformismo ***")
print("\nClase padre animal: ")
animal1 = Animal()
animal1.hacer_sonido()

print("\nClase Hija Perro: ")
animal2 = Perro()
animal2.hacer_sonido()

print("\nClase Hija Gato: ")
animal3 = Gato()
animal3.hacer_sonido()