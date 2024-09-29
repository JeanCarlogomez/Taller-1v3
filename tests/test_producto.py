from app.producto import Producto
from app.categoria import Categoria

def test_producto():
    print("Pruebas de la clase Producto")
    
    categoria = Categoria("Electrónica", "Dispositivos electrónicos")
    producto = Producto("Laptop", "Laptop de alta gama", 1200.00, 10, categoria)

    # Probar agregar stock
    producto.agregar_stock(5)
    assert producto.stock_inicial == 15, "Error: El stock no se actualizó correctamente después de agregar."

    # Probar retirar stock
    producto.retirar_stock(3)
    assert producto.stock_inicial == 12, "Error: El stock no se actualizó correctamente después de retirar."

    # Probar retirar más stock del disponible
    try:
        producto.retirar_stock(15)
    except ValueError:
        print("Correcto: No se puede retirar más stock del disponible.")

    # Probar calcular valor total
    valor_total = producto.calcular_valor_total()
    assert valor_total == 14400.00, "Error: El valor total calculado es incorrecto."
    print("Todas las pruebas de Producto pasaron.\n")

if __name__ == "__main__":
    test_producto()
