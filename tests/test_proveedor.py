from app.proveedor import Proveedor
from app.producto import Producto

def test_proveedor():
    print("Pruebas de la clase Proveedor")

    proveedor = Proveedor("Tech Supply", "123 Tech St", "555-1234")
    producto = Producto("Laptop", "Laptop de alta gama", 1200.00, 10, None)
    proveedor.agregar_producto(producto)

    # Cambia 'productos' por 'lista_productos'
    assert producto in proveedor.lista_productos, "Error: El producto no fue agregado correctamente al proveedor."
    print("Todas las pruebas de Proveedor pasaron.\n")

if __name__ == "__main__":
    test_proveedor()
