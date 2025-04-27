
class Aritmetica:

   
    def __init__(self, operando1=None, operando2=None):         
        self.operando1 = operando1
        self.operando2 = operando2


    def sumar(self):
       resultado = self.operando1 + self.operando2
       print(f'Resultado de la suma: {resultado}')
        
    def resta(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado de la Resta: {resultado}')
        
    def multiplicacion(self):
       resultado = self.operando1 * self.operando2
       print(f'Resultado de la Multiplicacion: {resultado}')
        
    def divicion(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado de la Divicion: {resultado}')

# Programa principal  
if __name__ == '__main__':
    print('*** Ejemplo de Aritmetica ***')
    aritmetica1 = Aritmetica(10, 23)
    aritmetica1.sumar()
    aritmetica1.resta()
    print()
    aritmetica2 = Aritmetica(12, 6)
    aritmetica2.sumar()
    aritmetica2.resta()
    print()
    aritmetica3 = Aritmetica(6)
    aritmetica3.operando2 = 7
    aritmetica3.sumar()
    print()
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 7
    aritmetica4.operando2 = 6
    aritmetica4.sumar()
    print()
    aritmetica5 = Aritmetica(operando1=4, operando2=3)
    aritmetica5.sumar()