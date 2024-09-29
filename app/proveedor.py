from .producto import Producto

class Proveedor:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.lista_productos = []
    
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
    
    def eliminar_producto(self, producto):
        if producto in self.lista_productos:
            self.lista_productos.remove(producto)
        else:
            raise ValueError(f"Producto {producto.nombre} no encontrado en la lista del proveedor")
    
    def listar_productos(self):
        return [producto.nombre for producto in self.lista_productos]
