from reto_mundo_pc.dispocitivos_entrada import DispositivoEntrada 

class Raton(DispositivoEntrada):

    contador_ratones = 0

    #constructor
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada
        super(). __init__(marca, tipo_entrada)


    def __str__(self,):
        return f'Id: {self.id_raton}, marca: {self.marca}, Tipo Entrada: {self.tipo_emtrada}'
    
# Codigo principal 
if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1 )