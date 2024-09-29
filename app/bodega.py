from producto import Producto

class Bodega:
    def __init__(self, nombre: str, ubicacion: str, capacidad_maxima: int):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = {}  # Diccionario {Producto: Cantidad}
    
    def agregar_producto(self, producto, cantidad: int):
        if self.obtener_total_stock() + cantidad > self.capacidad_maxima:
            raise ValueError("No hay suficiente capacidad en la bodega")
        if producto in self.productos_almacenados:
            self.productos_almacenados[producto] += cantidad
        else:
            self.productos_almacenados[producto] = cantidad
    
    def retirar_producto(self, producto, cantidad: int):
        if producto in self.productos_almacenados:
            if self.productos_almacenados[producto] >= cantidad:
                self.productos_almacenados[producto] -= cantidad
                if self.productos_almacenados[producto] == 0:
                    del self.productos_almacenados[producto]
            else:
                raise ValueError("Cantidad solicitada excede el stock disponible")
        else:
            raise ValueError(f"El producto {producto.nombre} no está almacenado en la bodega")
    
    def consultar_disponibilidad(self, producto):
        return self.productos_almacenados.get(producto, 0)

    def obtener_total_stock(self):
        return sum(self.productos_almacenados.values())
