# Definicion de una persona
class Persona:


    def inicializar_opersona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primier objeto
    persona1 = Persona() # Crea un objeto vacio en la memoria
    persona1.inicializar_opersona('Layla', 'Acosta')
    persona1.mostrar_persona()