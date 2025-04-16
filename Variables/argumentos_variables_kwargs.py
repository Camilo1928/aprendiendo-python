# *args - arguments - tupla
# **kwargs - keyword - arguments (key,value) como un diccionario

print("*** Argumentos variables en forma de un diccionario ***")

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f"Superheroe: {nombre} - {args} - Mas info: {kwargs}")

# Llamar la funcion 
superheroe_superpoderes("spiderman", "instinto Aracnido", edad=17, empresa="Marvel")
superheroe_superpoderes("Ironman", "Armadura", edad=45)

# Es opcinal enviar argumentos variables
superheroe_superpoderes("Mi vesino")