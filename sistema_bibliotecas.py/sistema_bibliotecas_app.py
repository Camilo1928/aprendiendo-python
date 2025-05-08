from sistema_bibliotecas.biblioteca import Biblioteca
from sistema_bibliotecas.libros import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional') 
print(f"*** Bienvenidos a la {bibliotecaNacional.nombre} ***")

# Definicion de libros
libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Ficcion")
libro2 = Libro("Don Quijote de la Mancha", "Migel de Cervates", "Comedia")
libro3 = Libro("El amor de los tiempos de colera", "Gabriel Garcia Marquez", "Ficcion")
libro4 = Libro("Pedro Paramo", "Juan Rulfo", "Ficcion")
libro5 = Libro("Pantaleon y los visitadores", "Mario Vargas Llosa", "Comedia")


# Agregamos los libros a la binblioteca
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

# Buscar libros por autor
autor = "Gabriel Garcia Marquez"
print(f"\nLibros de  {autor}")
bibliotecaNacional.buscar_libros_por_autor(autor)