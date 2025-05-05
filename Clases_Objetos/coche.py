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
        
    # def get_marca(self):
    #   return self._marca

    @property # Definir el metodo get de maneraaa mas paythonica
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

# Programa principal
if __name__ == '__main__':
    #Creacion de un primer coche
    coche1 = Coche('Toyata', 'Yaris', 'Azul')
    coche1.conducir_coche()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2' # Esto no es una buena practica
    coche1.color = 'Azul 2' # ignoro la modificacion
    # con setattr agregamos un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'valor nuevo atributo 2')
    # con el comando de __dict__ mostramos todos los valores del atributo de coche
    print(f'Atributos del cohce1: {coche1.__dict__}')
    coche1.conducir_coche()
    print(coche1.nuevo_atributo)
    print(f'Nuevo atributo coche1 {coche1.nuevo_atributo}')
  
   # Segundo objeto 
    coche2 = Coche('chevrolet', 'Trax', 'Blanco')
    coche2.conducir_coche()
    # con el comando de __dict__ mostramos todos los aributos de nuestra clase
    print(f'Atributo del coche1: {coche2.__dict__}')