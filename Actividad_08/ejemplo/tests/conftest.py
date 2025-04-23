import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

@pytest.fixture
def carrito():
    return Carrito()

@pytest.fixture
def producto_generico():
    return ProductoFactory(nombre="Producto", precio=100.00)
