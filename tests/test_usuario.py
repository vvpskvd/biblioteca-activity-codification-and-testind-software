import pytest
from src.usuario import Usuario
from src.libro import Libro

def test_crear_usuario():
    u = Usuario(1, "Daniel")
    assert u.nombre == "Daniel"
    assert u.libros_prestados == []

def test_usuario_presta_libro():
    u = Usuario(1, "Ana")
    libro = Libro("01", "1984", "Orwell")
    u.libros_prestados.append(libro)
    assert len(u.libros_prestados) == 1

def test_ids_diferentes():
    u1 = Usuario(1, "A")
    u2 = Usuario(2, "B")
    assert u1.id != u2.id

def test_repr_usuario():
    u = Usuario(3, "Juan")
    assert "Juan" in str(u.__dict__)

def test_agregar_multiples_libros():
    u = Usuario(4, "Luz")
    for i in range(3):
        u.libros_prestados.append(Libro(str(i), f"L{i}", "X"))
    assert len(u.libros_prestados) == 3