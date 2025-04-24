
















# ESTA ES MI CALCULADORA 
print("*** Calculadora de impuestos ***")

def cualculadora_impuestos():
    pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
    monto_del_impuesto = int(input("Proporcione el monto del impuesto: "))
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (monto_del_impuesto/100)
    print(f"Pago con impuesto: {pago_total}")

cualculadora_impuestos()


# ESTA ES LA QUE SOLUCIONA EL EJERCIO DEL VIDEO 
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pago_sin_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_sin_impuesto}')


# Y ESTA ES LA QUE ME RECOMIENDA CHATGPT
def calcular_total_pago(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)

def calculadora_interactiva():
    print("*** Calculadora de impuestos ***")
    try:
        pago = float(input('Proporcione el pago sin impuesto: '))
        impuesto = float(input('Proporcione el monto del impuesto (%): '))
        total = calcular_total_pago(pago, impuesto)
        print(f'Pago con impuesto: {total:.2f}')
    except ValueError:
        print("Error: ingresa valores numéricos válidos.")

# Programa principal
if __name__ == '__main__':
    calculadora_interactiva()
