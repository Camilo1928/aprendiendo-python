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
        print(f'''Persona:
            Marca: {self.marca}
            Modelo: {self.modelo}''')
        
if __name__ == '__main__':
        carro1 = Carro('Mazda', 2025)
        # ya no utilizamos el metodo de unicializar_persona sino que al momento de crear 
        # el objeto se manda a llamar de manera automatica el metodo __init__
        carro1.mostrar_carro()
        # diferencia importante; desde el momneto en que estamos creando nuestro objeto, 
        # se estan inicializando los atributos de nuestra class
        carro2 = Carro('Hiundai', 2024) 