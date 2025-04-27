# Creamos nuestra class

class Aritmetica:

   
    def __init__(self, operando1, operando2):         
        self.operando1 = operando1
        self.operando2 = operando2


    def sumar(self):
       
        print(f'''Suma:
            Numero1: {self.operando1} 
            Numero2: {self.operando2}
            Suma: {self.operando1 + self.operando2}
              ''')
        
    def resta(self):
        print(f'''Resta:
            Numero: {self.operando1}
            Numero: {self.operando2}
            Resta: {self.operando1 - self.operando2}
            ''')
        
    def multiplicacion(self):
        print(f'''Multiplicacion:
            Numero: {self.operando1}
            Numero: {self.operando2}
            Multiplicacion: {self.operando1 * self.operando2}
            ''')
        
    def divicion(self):
        print(f'''Divicion:
            Numero: {self.operando1}
            Numero: {self.operando2}
            Divicion: {self.operando1 / self.operando2}''')
            

# Programa principal  
if __name__ == '__main__':
    sumar = Aritmetica(5, 7)
    sumar.sumar()


    Aritmetica2 = Aritmetica(10, 2)
    Aritmetica2.resta()

    Aritmetica2 = Aritmetica(2, 10)
    Aritmetica2.multiplicacion()

    Aritmetica2 = Aritmetica(50, 2)
    Aritmetica2.divicion()



# Creamos nuestra class



class Aritmetica:

   
    def __init__(self, operando1, operando2):         
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
    aritmetica3 = Aritmetica(6,12)
    aritmetica3.multiplicacion()
    print()
    aritmetica4 = Aritmetica(56, 2)
    aritmetica4.divicion()