import pytest
from src.libro import Libro

def test_crear_libro():
    libro = Libro("001", "1984", "Orwell")
    assert libro.titulo == "1984"
    assert libro.autor == "Orwell"
    assert libro.disponible is True

def test_libro_no_disponible():
    libro = Libro("002", "Dune", "Herbert", disponible=False)
    assert not libro.disponible

def test_isbn_unico():
    libro1 = Libro("001", "Test1", "A")
    libro2 = Libro("002", "Test2", "B")
    assert libro1.isbn != libro2.isbn

def test_str_representacion():
    libro = Libro("003", "It", "King")
    assert "It" in str(libro.__dict__)

def test_disponibilidad_modificable():
    libro = Libro("004", "HP", "Rowling")
    libro.disponible = False
    assert libro.disponible is False