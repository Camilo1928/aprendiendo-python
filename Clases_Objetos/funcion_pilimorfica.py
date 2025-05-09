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

# FUNCION POLIMORFICA
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

print("*** Ejemplo Poliformismo ***")
print("\nClase padre animal: ")
animal1 = Animal()
hacer_sonido_animal(animal1)
# animal1.hacer_sonido()

print("\nClase Hija Perro: ")
perro1 = Perro()
hacer_sonido_animal(perro1)
# perro1.hacer_sonido()

print("\nClase Hija Gato: ")
gato1 = Gato()
hacer_sonido_animal(perro1)
# gato1.hacer_sonido()