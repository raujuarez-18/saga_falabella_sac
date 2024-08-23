class Detalle_Comercial:
    def __init__(self, precio, cantidad):
        self.__precio = precio
        self.__cantidad = cantidad
    
    def set_precio(self, precio):
        self.__precio = precio
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def get_precio(self):
        return self.__precio
    def get_cantida(self):
        return self.__cantidad