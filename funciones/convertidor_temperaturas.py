
# Funcion que combierte celsius a fehrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Funcion que combierte fahrenheit a celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9

# Realizamos algunas pruebas de conversion
c = float(input("Proporcione su valor en celsius: "))
resultado = celsius_fahrenheit(c)
# Imprimimo la funcion
print(f"{c} C a F: {resultado:.2f}")


# Realizamos la prueba de grados fahrenheit a celius
f = float(input(f"Proporcione su valor en fahrenheit: "))
resultado = fahrenheit_a_celsius(f)
# Imprimimos el resultado
print(f'{f} F a C: {resultado:0.2f}')