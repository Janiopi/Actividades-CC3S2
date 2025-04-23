## Ejemplo de prueba
# tests/test_carrito.py

import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

def test_agregar_producto_nuevo(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    # Arrange
    carrito.agregar_producto(producto_generico)

    # Act
    items = carrito.obtener_items()
    
    # Assert
    
    assert len(items) == 1
    assert items[0].producto.nombre == "Producto"
    


def test_agregar_producto_existente_incrementa_cantidad(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto_generico, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito.agregar_producto(producto_generico,cantidad=3)
    
    # Act
    carrito.remover_producto(producto_generico, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)
    
    # Act
    carrito.remover_producto(producto_generico, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


@pytest.mark.parametrize(
    "cantidad_inicial, cantidad_a_actualizar, cantidad_esperada",
    [
        (5, 3, 3),
        (10, 5, 5),
        (2, 2, 2),
    ]
)
def test_actualizar_cantidad_producto(cantidad_inicial,cantidad_a_actualizar,cantidad_esperada):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Producto", precio=100)
    carrito.agregar_producto(producto, cantidad=cantidad_inicial)
    
    # Act
    carrito.actualizar_cantidad(producto, cantidad_a_actualizar)
    
    # Assert
    items = carrito.obtener_items()
    assert items[0].cantidad == cantidad_esperada


def test_actualizar_cantidad_a_cero_remueve_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Cargador", precio=25.00,stock=5)
    carrito.agregar_producto(producto, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 550.00


@pytest.mark.parametrize(
    "total, descuento, resultado_esperado",
    [
        (1000, 10, 900),
        (200, 20, 160),
        (500, 50, 250),
    ]
)
def test_aplicar_descuento(total, descuento, resultado_esperado):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Producto", precio=total)
    carrito.agregar_producto(producto, cantidad=1)  
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(descuento)
    
    # Assert
    assert total_con_descuento == resultado_esperado


def test_aplicar_descuento_limites():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)

def test_vaciar_carrito():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act: Se vacía el carrito.
    Assert: Se verifica que el carrito esté vacío.
    """
    #Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.00)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=2)
    # Act
    carrito.vaciar()
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0
    assert carrito.calcular_total() == 0.00

def test_descuento_condicional():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos.
    Act: Se aplica un descuento del 20% si el total supera 500.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.00)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto1, cantidad=1)  # Total 1000
    carrito.agregar_producto(producto2, cantidad=2)  # Total 1100
    
    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(20,500)
    
    # Assert
    assert total_con_descuento == 880.00
def test_descuento_condicional_no_aplica():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan productos.
    Act: Se aplica un descuento del 20% si el total no supera 500.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Mouse", precio=50.00)
    producto2 = ProductoFactory(nombre="Teclado", precio=75.00)
    carrito.agregar_producto(producto1, cantidad=1)  # Total 50
    carrito.agregar_producto(producto2, cantidad=2)  # Total 200
    # Act
    total_con_descuento = carrito.aplicar_descuento_condicional(20,500)
    # Assert
    assert total_con_descuento == 200.00
    
def test_agregar_producto_excede_stock():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto con stock limitado.
    Act: Se intenta agregar una cantidad mayor al stock disponible.
    Assert: Se verifica que se lanza un ValueError.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00, stock=5)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=10)

def test_agregar_producto_no_excede_stock():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto con stock limitado.
    Act: Se intenta agregar una cantidad menor o igual al stock disponible.
    Assert: Se verifica que no se lanza un ValueError.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00, stock=5)
    # Act
    carrito.agregar_producto(producto, cantidad=5)
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1

def test_obtener_items_ordenados_precio():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act: Se obtienen los items del carrito ordenados por nombre.
    Assert: Se verifica que los items estén ordenados correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.00)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=2)
    
    # Act
    items = carrito.obtener_items_ordenados("precio")
    
    # Assert
    assert len(items) == 2
    assert items[0].producto.nombre == "Mouse"
    assert items[1].producto.nombre == "Laptop"


def test_obtener_items_ordenados_nombre():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act: Se obtienen los items del carrito ordenados por nombre.
    Assert: Se verifica que los items estén ordenados correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.00)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=2)
    
    # Act
    items = carrito.obtener_items_ordenados("nombre")
    
    # Assert
    assert len(items) == 2
    assert items[0].producto.nombre == "Laptop"
    assert items[1].producto.nombre == "Mouse"

def test_obtener_items_ordenados_stock():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos.
    Act: Se obtienen los items del carrito ordenados por stock.
    Assert: Se verifica que los items estén ordenados correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=1000.00,stock=5)
    producto2 = ProductoFactory(nombre="Mouse", precio=50.00,stock=6)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=2)
    
    # Act
    items = carrito.obtener_items_ordenados("nombre")
    
    # Assert
    assert len(items) == 2
    assert items[0].producto.nombre == "Laptop"
    assert items[1].producto.nombre == "Mouse"


