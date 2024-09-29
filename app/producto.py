class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock_inicial = stock_inicial
        self.categoria = categoria
    
    def agregar_stock(self, cantidad):
        self.stock_inicial += cantidad
    
    def retirar_stock(self, cantidad):
        if cantidad <= self.stock_inicial:
            self.stock_inicial -= cantidad
        else:
            raise ValueError("No hay suficiente stock")
    
    def calcular_valor_total(self):
        return self.stock_inicial * self.precio
