print('*** Alcanse de Variables ***')

# Variable global
contador_global = 0

def incrementar_contador():
    #declaramos una variale local
    variable_local = 0

    # usar la variable global
    global contador_global 
    #incrementamos la variable global
    contador_global += 1
    # incrementamos la variable local
    variable_local += 1

    # imprimimso ambos contadores
    print(f"contador local: {variable_local}")
    print(f"contador global: {contador_global}\n")

# llamamos varis veces la funcion 
incrementar_contador();
incrementar_contador();
incrementar_contador();

print(f"valor variable global: {contador_global}")