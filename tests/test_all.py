import unittest
from app.producto import Producto
from app.categoria import Categoria
from app.proveedor import Proveedor
from app.bodega import Bodega

class TestSistemaGestion(unittest.TestCase):

    def setUp(self):
        # Crear una categoría
        self.categoria = Categoria("Electrónica", "Dispositivos electrónicos")
        
        # Crear productos
        self.producto1 = Producto("Laptop", "Laptop de alta gama", 1200.00, 10, self.categoria)
        self.producto2 = Producto("Smartphone", "Teléfono inteligente", 800.00, 20, self.categoria)

        # Agregar productos a la categoría
        self.categoria.agregar_producto(self.producto1)
        self.categoria.agregar_producto(self.producto2)

        # Crear un proveedor
        self.proveedor = Proveedor("Tech Supply", "123 Tech St", "555-1234")
        self.proveedor.agregar_producto(self.producto1)
        self.proveedor.agregar_producto(self.producto2)

        # Crear una bodega
        self.bodega = Bodega("Bodega Central", "Av. Principal 100", 500)
        self.bodega.agregar_producto(self.producto1, 10)
        self.bodega.agregar_producto(self.producto2, 20)

    def test_agregar_stock_producto(self):
        self.producto1.agregar_stock(5)
        self.assertEqual(self.producto1.stock_inicial, 15)

    def test_retirar_stock_producto(self):
        self.producto2.retirar_stock(5)
        self.assertEqual(self.producto2.stock_inicial, 15)

    def test_retirar_stock_insuficiente(self):
        with self.assertRaises(ValueError):
            self.producto1.retirar_stock(20)

    def test_calcular_valor_total_producto(self):
        valor_total = self.producto1.calcular_valor_total()
        self.assertEqual(valor_total, 12000.00)

    def test_listar_productos_categoria(self):
        productos = self.categoria.listar_productos()
        self.assertIn("Laptop", productos)
        self.assertIn("Smartphone", productos)

    def test_consultar_disponibilidad_bodega(self):
        disponibilidad = self.bodega.consultar_disponibilidad(self.producto1)
        self.assertEqual(disponibilidad, 10)

    def test_retirar_producto_bodega(self):
        self.bodega.retirar_producto(self.producto2, 5)
        self.assertEqual(self.bodega.consultar_disponibilidad(self.producto2), 15)

if __name__ == "__main__":
    unittest.main()
