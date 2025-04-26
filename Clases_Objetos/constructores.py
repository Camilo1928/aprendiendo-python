# Definicion de un constructor

class Carro:


    # Constructor 
    # Un constructor nos permite crear nuestro objeto, ademas de crear los atributos y tambien 
    # de manera occional inicializar sus valores
    def __init__(self, marca, modelo):
        # Creamos los atributos de la class
        self.marca = marca
        self.modelo = modelo

    def mostrar_carro(self):
        print(f'''Carro:
        Marca: {self.marca}
        Modelo: {self.modelo}''')
        print(f'Dir. men self: {id(self)}')
        print(f'Dir. men hex self: {hex(id(self))}')
        
if __name__ == '__main__':
        carro1 = Carro('Mazda', 2025)
        # ya no utilizamos el metodo de unicializar_persona sino que al momento de crear 
        # el objeto se manda a llamar de manera automatica el metodo __init__
        carro1.mostrar_carro()
        # diferencia importante; desde el momneto en que estamos creando nuestro objeto, 
        # se estan inicializando los atributos de nuestra class
        print(f'Dir. men carro1: {id(carro1)}')
        print(f'Dir. men hex carro1: {hex(id(carro1))}')


        carro2 = Carro('Hiundai', 2024) 
        carro2.mostrar_carro()
        print(f'Dir. men carro2: {id(carro2)}')
        print(f'Dir. men hex carro2: {hex(id(carro2))}')

def invertir_palabra(palabra):
     pass