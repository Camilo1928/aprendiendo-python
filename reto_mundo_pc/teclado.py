from reto_mundo_pc.dispocitivos_entreda import DispocitivoEntrada


class Teclado(DispocitivoEntrada):

    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'Id: {self.id_teclado}, Marca: {self.marca}, Tipo_entrada: {self.tipo_entrada}')

# Codigo Principal
# teclado1 = Teclado('Dell', 'USB')
# print(teclado1)
# teclado2 = Teclado('Asus', 'USB')
# print(teclado2)
