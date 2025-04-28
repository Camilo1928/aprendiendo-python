# Definimos la clase
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributos protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir_coche(self):
        print(F'''Conducioendo el coche:
              Marca: {self._marca}
              Modelo: {self._modelo}
              Color: {self._color}''')
        
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

# Programa principal
if __name__ == '__main__':
    #Creacion de un primer coche
    coche1 = Coche('Toyata', 'Yaris', 'Azul')
    coche1.conducir_coche()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.set_marca('Toyota 2')
    coche1.set_modelo('Yaris 2') # Esto no es una buena practica
    coche1.set_color('Azul 2') # ignoro la modificacion


    #coche1._Coche__color = ('Azul 3') # ES UNA MALA PARCTICA POR FAVOR NO HACERLO
    coche1.conducir_coche()