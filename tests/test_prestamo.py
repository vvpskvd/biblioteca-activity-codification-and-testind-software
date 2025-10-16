import pytest
from datetime import date
from src.libro import Libro
from src.usuario import Usuario
from src.prestamo import Prestamo

def test_crear_prestamo():
    l = Libro("001", "HP", "Rowling")
    u = Usuario(1, "Ana")
    p = Prestamo(1, l, u, date.today())
    assert p.libro.titulo == "HP"
    assert p.fecha_devolucion is None

def test_devolucion_prestamo():
    l = Libro("002", "Dune", "Herbert")
    u = Usuario(2, "Carlos")
    p = Prestamo(2, l, u, date.today())
    p.fecha_devolucion = date.today()
    assert p.fecha_devolucion == date.today()

def test_ids_diferentes():
    l = Libro("1", "A", "B")
    u = Usuario(1, "U")
    p1 = Prestamo(1, l, u, date.today())
    p2 = Prestamo(2, l, u, date.today())
    assert p1.id != p2.id

def test_relacion_usuario_libro():
    l = Libro("5", "Moby Dick", "Melville")
    u = Usuario(6, "Raul")
    p = Prestamo(1, l, u, date.today())
    assert isinstance(p.usuario, Usuario)

def test_repr_prestamo():
    l = Libro("9", "It", "King")
    u = Usuario(9, "Luis")
    p = Prestamo(1, l, u, date.today())
    assert "King" in str(p.libro.autor)