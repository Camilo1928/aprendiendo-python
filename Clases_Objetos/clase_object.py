class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Sobreescribimos el metodo __str__
    def __str__(self):
        return f'''Persona
        nombre = {self.nombre}
        apellido = {self.apellido}
        dir.men {super.__str__(self)}'''


# Codigo principal 
persona1 = Persona('Ana', 'Martinez')
print(persona1) # El metodo ___str___ se llama automatica mente desde print
# print(persona1.__str__()) Esto es opcional