from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega

def main():
    categoria = Categoria("Electrónica", "Dispositivos electrónicos")
    producto1 = Producto("Laptop", "Laptop de alta gama", 1200.00, 10, categoria)
    producto2 = Producto("Smartphone", "Teléfono inteligente", 800.00, 20, categoria)
    categoria.agregar_producto(producto1)
    categoria.agregar_producto(producto2)
    proveedor = Proveedor("Tech Supply", "123 Tech St", "555-1234")
    proveedor.agregar_producto(producto1)
    proveedor.agregar_producto(producto2)
    bodega = Bodega("Bodega Central", "Av. Principal 100", 500)
    bodega.agregar_producto(producto1, 10)
    bodega.agregar_producto(producto2, 20)
    print(f"Stock de {producto1.nombre} en {bodega.nombre}: {bodega.consultar_disponibilidad(producto1)}")
    print(f"Stock de {producto2.nombre} en {bodega.nombre}: {bodega.consultar_disponibilidad(producto2)}")

    try:
        bodega.retirar_producto(producto1, 5)
        print(f"Stock de {producto1.nombre} después de retirar: {bodega.consultar_disponibilidad(producto1)}")
    except ValueError as e:
        print(e)

    valor_total_laptop = producto1.calcular_valor_total()
    print(f"Valor total del stock de {producto1.nombre}: {valor_total_laptop}")

    print(f"Productos en la categoría {categoria.nombre}: {categoria.listar_productos()}")

if __name__ == "__main__":
    main()
