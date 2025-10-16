class Prestamo:
    def __init__(self, id, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion