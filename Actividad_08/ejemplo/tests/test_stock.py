# tests/test_stock.py
import pytest
from src.carrito import Carrito, Producto

def test_agregar_producto_excede_stock():
    # Arrange: Suponemos que el producto tiene 5 unidades en stock.
    producto = Producto("ProductoStock", 100.00, 5)
    producto.stock = 5
    carrito = Carrito()

    # Act & Assert: Se lanza una excepción al intentar agregar más de 5
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=6)
