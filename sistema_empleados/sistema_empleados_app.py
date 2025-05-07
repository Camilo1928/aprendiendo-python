from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

print("*** Sistema de Empleados ***")


# Creamos una instancia de una empresa
empresa1 = Empresa('Global Mentoring')

# Contratar algunos empleados 
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')


# obtener el total de objetos de tipo empleados 
print(f"Total de empleados: {Empleado.obtener_total_empleados()}")

# obtener el numero de empleados en el departamento de ventas
print(f"Empleados en el departamento de ventas: "
      f"{empresa1.obtener_numero_empleados_departamento('Ventas')}")

# Mostramos todos los empleados de la empresa
empresa1.obtener_total_empleados()