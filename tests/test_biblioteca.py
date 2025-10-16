import pytest
from datetime import date
from src.biblioteca import Biblioteca
from src.libro import Libro
from src.usuario import Usuario

@pytest.fixture
def setup_biblioteca():
    b = Biblioteca()
    libro = Libro("001", "1984", "Orwell")
    usuario = Usuario(1, "Ana")
    b.agregar_libro(libro)
    b.registrar_usuario(usuario)
    return b, libro, usuario



def test_agregar_libro(setup_biblioteca):
    b, _, _ = setup_biblioteca
    assert len(b.catalogo) == 1

def test_registrar_usuario(setup_biblioteca):
    b, _, _ = setup_biblioteca
    assert len(b.usuarios) == 1

def test_prestar_libro(setup_biblioteca):
    b, libro, usuario = setup_biblioteca
    prestamo = b.prestar_libro("001", 1, date.today())
    assert prestamo.libro.disponible is False
    assert len(b.prestamos) == 1

def test_devolver_libro(setup_biblioteca):
    b, libro, usuario = setup_biblioteca
    b.prestar_libro("001", 1, date.today())
    result = b.devolver_libro("001", 1, date.today())
    assert result is True
    assert libro.disponible is True

def test_buscar_libro(setup_biblioteca):
    b, _, _ = setup_biblioteca
    result = b.buscar_libro("1984")
    assert len(result) == 1



def test_excepcion_prestar_libro_invalido(setup_biblioteca):
    b, _, _ = setup_biblioteca
    with pytest.raises(ValueError):
        b.prestar_libro("999", 1, date.today())

def test_excepcion_usuario_invalido(setup_biblioteca):
    b, _, _ = setup_biblioteca
    with pytest.raises(ValueError):
        b.prestar_libro("001", 99, date.today())

def test_excepcion_devolucion_inexistente(setup_biblioteca):
    b, _, _ = setup_biblioteca
    with pytest.raises(ValueError):
        b.devolver_libro("001", 1, date.today())



@pytest.mark.parametrize("texto,esperado", [
    ("1984", 1),
    ("Orwell", 1),
    ("NoExiste", 0)
])
def test_buscar_libro_parametrizado(texto, esperado):
    b = Biblioteca()
    b.agregar_libro(Libro("001", "1984", "Orwell"))
    assert len(b.buscar_libro(texto)) == esperado