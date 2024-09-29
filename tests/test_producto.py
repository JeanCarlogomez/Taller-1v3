from app.producto import Producto

def test_crear_producto():
    producto = Producto("Manzana", 10)
    assert producto.nombre == "Manzana"
    assert producto.cantidad == 10

def test_actualizar_cantidad():
    producto = Producto("Manzana", 10)
    producto.actualizar_cantidad(5)
    assert producto.cantidad == 15

def test_crear_producto_invalid():
    try:
        Producto("", -5)  # Esto debería fallar
        assert False, "Se esperaba un error al crear un producto con datos inválidos."
    except ValueError:
        pass  # Se espera que se lance un ValueError
