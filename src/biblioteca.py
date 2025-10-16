from .prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, isbn, id_usuario, fecha):
        libro = next((l for l in self.catalogo if l.isbn == isbn and l.disponible), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        if not libro or not usuario:
            raise ValueError("Libro o usuario no válido")
        libro.disponible = False
        prestamo = Prestamo(len(self.prestamos)+1, libro, usuario, fecha)
        self.prestamos.append(prestamo)
        usuario.libros_prestados.append(libro)
        return prestamo

    def devolver_libro(self, isbn, id_usuario, fecha):
        prestamo = next(
            (p for p in self.prestamos if p.libro.isbn == isbn and p.usuario.id == id_usuario and not p.fecha_devolucion),
            None
        )
        if not prestamo:
            raise ValueError("No existe préstamo activo para este libro y usuario")
        prestamo.fecha_devolucion = fecha
        prestamo.libro.disponible = True
        prestamo.usuario.libros_prestados.remove(prestamo.libro)
        return True

    def buscar_libro(self, texto):
        return [l for l in self.catalogo if texto.lower() in l.titulo.lower() or texto.lower() in l.autor.lower()]
