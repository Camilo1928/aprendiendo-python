class Persona:

    contador_personas = 0

    def __init__(self, nombre, apellido):
        # iNCREMENTAMOS EL VALOR DEL ATRIBUTO DE CLASE
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostar_persona(self):
        print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")

    @staticmethod
    def get_contador_personas_estatico():
        print("Metodo estatico")
        return Persona.contador_personas
    
    @classmethod
    def get_contador_personas_clase(cls):
        print('Metodo de clase')
        return cls.contador_personas

if __name__ == '__main__':
    print("*** Ejemplo contador de objetos de tipo persona ***")
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostar_persona()

    # Segundo objeto 
    persona2 = Persona('Daniel', 'Sanachez')
    persona2.mostar_persona()

    # Tercer objeto
    persona3 = Persona('kevin', 'Rivera')
    persona3.mostar_persona()

    # Imprimir el valor del contador personas
    print(f"Contador objetos Persona: {Persona.contador_personas}")
    print(f"Contador objetos Persona (perona1): {persona1.contador_personas}")
    print(f"Contador objetos persona (static): {Persona.get_contador_personas_estatico()}")
    print(f"Contador objeto Persona (clase): {Persona.get_contador_personas_clase()}")