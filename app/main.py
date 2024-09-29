from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega

def main():
    # Crear una categoría
    categoria = Categoria("Electrónica", "Dispositivos electrónicos")

    # Crear productos
    producto1 = Producto("Laptop", "Laptop de alta gama", 1200.00, 10, categoria)
    producto2 = Producto("Smartphone", "Teléfono inteligente", 800.00, 20, categoria)

    # Agregar productos a la categoría
    categoria.agregar_producto(producto1)
    categoria.agregar_producto(producto2)

    # Crear un proveedor
    proveedor = Proveedor("Tech Supply", "123 Tech St", "555-1234")
    proveedor.agregar_producto(producto1)
    proveedor.agregar_producto(producto2)

    # Crear una bodega
    bodega = Bodega("Bodega Central", "Av. Principal 100", 500)
    bodega.agregar_producto(producto1, 10)
    bodega.agregar_producto(producto2, 20)

    # Consultar disponibilidad en la bodega
    print(f"Stock de {producto1.nombre} en {bodega.nombre}: {bodega.consultar_disponibilidad(producto1)}")
    print(f"Stock de {producto2.nombre} en {bodega.nombre}: {bodega.consultar_disponibilidad(producto2)}")

    # Intentar retirar productos
    try:
        bodega.retirar_producto(producto1, 5)
        print(f"Stock de {producto1.nombre} después de retirar: {bodega.consultar_disponibilidad(producto1)}")
    except ValueError as e:
        print(e)

    # Consultar el valor total del stock de un producto
    print(f"Valor total del stock de {producto1.nombre}: {producto1.calcular_valor_total()}")

    # Listar productos en la categoría
    print(f"Productos en la categoría {categoria.nombre}: {categoria.listar_productos()}")

if __name__ == "__main__":
    main()
