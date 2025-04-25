# Defincion de una clase
class Persona:

    # Definicion de una clase 
    def inicializar_persona(self, nombre, apellido):
        # Creanos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''') 


# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona() # Creamos un objeto vacio en memori
    persona1.inicializar_persona('Kevin', 'Rivera') # Crear un objeto vacio en memoria
    persona1.mostrar_persona()
    
    persona2 = Persona()
    persona2.inicializar_persona('Noemi', 'Zambrano')
    persona2.mostrar_persona()


class Carro:

    def inicializar_carro(self, marca, modelo, color, ruedas, puertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas 
        self.puertas = puertas

    def mostrar_carro(self):
        print(f''' Carro:
        Marca: {self.marca}
        Modelo: {self.modelo}
        Color: {self.color}
        Ruedas: {self.ruedas}
        Puertas: {self.puertas}      
        ''')

if __name__ == '__main__':
    carro1 = Carro() 
    carro1.inicializar_carro('Mazda', 2017, 'Rojo', 4, 5)
    carro1.mostrar_carro()



class Computador():
    # Definimos nuestra clse
    def componentes_pc(self, boar, tarjeta_de_video, fuente_de_poder, ram, procesador, ssd):
        self.boar = boar
        self.tarjeta_de_video = tarjeta_de_video
        self.fuente_de_poder = fuente_de_poder
        self.ram = ram
        self.procesador = procesador
        self.ssd = ssd

    def mostrar_pc(self):
        print(f'''PC: 
        Boar: {self.boar}
        Tarjeta de video: {self.tarjeta_de_video}
        Fuente de poder: {self.fuente_de_poder}
        Ram: {self.ram}
        Procesador: {self.procesador}
        SSD: {self.ssd}''')

if __name__ == '__main__':
    pc_gamer = Computador()
    pc_gamer.componentes_pc('MSI 450A PRO', 'RADEOM 3040', '650-W REAL', 'DDR4', 'RAIZEN 5 - 5600', 'ZATA-500GB' )
    pc_gamer.mostrar_pc()

            
