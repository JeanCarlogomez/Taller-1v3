from .producto import Producto

class Categoria:
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            raise ValueError(f"Producto {producto.nombre} no encontrado en la categoría")

    def listar_productos(self):
        return [producto.nombre for producto in self.productos]
