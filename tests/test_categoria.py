from app.categoria import Categoria
from app.producto import Producto

def test_categoria():
    print("Pruebas de la clase Categoria")

    categoria = Categoria("Electrónica", "Dispositivos electrónicos")
    producto1 = Producto("Laptop", "Laptop de alta gama", 1200.00, 10, categoria)
    producto2 = Producto("Smartphone", "Teléfono inteligente", 800.00, 20, categoria)

    # Agregar productos a la categoría
    categoria.agregar_producto(producto1)
    categoria.agregar_producto(producto2)

    # Listar productos en la categoría
    productos = categoria.listar_productos()
    assert "Laptop" in productos, "Error: Laptop no está en la lista de productos."
    assert "Smartphone" in productos, "Error: Smartphone no está en la lista de productos."
    print("Todas las pruebas de Categoria pasaron.\n")

if __name__ == "__main__":
    test_categoria()
