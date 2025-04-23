import pytest
from unittest.mock import Mock
from src.shopping_cart import ShoppingCart



def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # nombre, cantidad, precio unitario
    assert cart.items == {"apple": {"quantity": 2, "unit_price": 0.5}}

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.remove_item("apple")
    assert cart.items == {}

def test_calculate_total():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    total = cart.calculate_total() - cart.discount
    assert total == 2*0.5 + 3*0.75  # 2*0.5 + 3*0.75 = 1 + 2.25 = 3.25

def test_apply_discount():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    cart.apply_discount(10)  # Descuento del 10%
    total = cart.calculate_total()
    expected_total = (2*0.5 + 3*0.75) * 0.9  # Aplicando 10% de descuento
    assert total == round(expected_total,2) 

def test_process_payment():
    # Creamos un Mock del servicio de pago
    payment_gateway = Mock()
    payment_gateway.process_payment.return_value = True  # Simulamos que el pago fue exitoso

    # Creamos el carrito de compras y lo configuramos
    cart = ShoppingCart(payment_gateway=payment_gateway)
    cart.add_item("apple", 2, 0.5)  # Agregamos artículos
    cart.add_item("banana", 3, 0.75)
    cart.apply_discount(10)  # Aplicamos un descuento del 10%

    total = cart.calculate_total()  # Calculamos el total
    result = cart.process_payment(total)  # Procesamos el pago

    # Verificamos que el método de pago fue llamado con el total
    payment_gateway.process_payment.assert_called_once_with(total)
    assert result == True  # Comprobamos que el resultado del pago sea True