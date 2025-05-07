class Empleado:

    # Para sabar cuantos objetos de tipo empleados se han creado
    contador_empleados = 0 # Atributo de clase por que esta fuero de los metodos de la clase
    
    def __init__(self, nombre, departamento):
        self.nombre = nombre # Metodo de instancia
        self.departamento = departamento # Metodo de instancia
        Empleado.contador_empleados += 1 # incrementamos la variable de contador empleados
        self.id = Empleado.contador_empleados


    @classmethod # Metodo de clase que nos permite acceder a los atributos de la clase
    def obtener_total_empleados(cls): # Esteme metodo se asocia a la clase en si misma y no con los objetos, por eso recivimos el parametro de (cls)
        return cls.contador_empleados