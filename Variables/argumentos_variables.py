print("*** Argumento Variables ***")

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f"superheroe: {superheroe} - {nombre} - {args}")
    
    #Iteramos los  superpoderes
    for superpoder in args:
        print(f"\tsuperpoder: {superpoder}")

superheroe_superpoderes("spiderman", "peter parker", "instinto aracnido", "Telaraña")
superheroe_superpoderes("Iroman", "Tony stark", "Armadura", "playboy", "Millonario")
superheroe_superpoderes("Mi vecino", "Juan pere")

print("*** Mi Propio Ejemplo ***")

def componentes_de_una_computadora(computadora, nombre, *args):
    print(f"Computadora: {computadora} - {nombre} - {args}")

# LLamar funcion
componentes_de_una_computadora("Janus", "MSI", "RAM DDR4, BOAR MSI A520-PRO-MAX, Graficas nvidia 3060")
