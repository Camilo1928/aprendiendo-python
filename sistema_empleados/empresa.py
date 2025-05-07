from sistema_empleados.empleado import Empleado


class Empresa:
    # metodo
    def __init__(self, nombre):
        self.nombre = nombre # aributo de nombre
        self.empleados = [] # atributo de empleados que es una lista, que almacena objetos de tipo empleado

    # motodo
    def contratar_empleado(self, nombre, departamento):
        empleado  = Empleado(nombre, departamento)  # importamos la clase de empleado ya que vamos a trabajar con ella  
        self.empleados.append(empleado) # agregamos a traves de la lista de empleados

    # metodo
    def obtener_numero_empleados_departamento(self, departamento):
        contador_empleados_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento: # iteramos nuestra lista de empleados 
                contador_empleados_por_departamento += 1 # incrementamo el valor de nuestra variable
        return contador_empleados_por_departamento
    
    def obtener_total_empleados(self):
        print(f"\nTotal de empleados para la empresa: {self.nombre}")
        for empleado in self.empleados:
            print(f"""Empleado {empleado.id}
                  Nombre: {empleado.nombre}
                  Departamento: {empleado.departamento}""")
