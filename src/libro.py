class Libro:
    def __init__(self, isbn, titulo, autor, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible