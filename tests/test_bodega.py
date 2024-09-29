from app.bodega import Bodega
from app.producto import Producto

def test_bodega():
    print("Pruebas de la clase Bodega")

    bodega = Bodega("Bodega Central", "Av. Principal 100", 500)
    producto = Producto("Laptop", "Laptop de alta gama", 1200.00, 10, None)
    bodega.agregar_producto(producto, 10)

    assert bodega.consultar_disponibilidad(producto) == 10, "Error: La disponibilidad no es correcta después de agregar."

    bodega.retirar_producto(producto, 5)
    assert bodega.consultar_disponibilidad(producto) == 5, "Error: La disponibilidad no se actualizó correctamente después de retirar."

    try:
        bodega.retirar_producto(producto, 10)
    except ValueError:
        print("Correcto: No se puede retirar más stock del disponible.")

    print("Todas las pruebas de Bodega pasaron.\n")

if __name__ == "__main__":
    test_bodega()
