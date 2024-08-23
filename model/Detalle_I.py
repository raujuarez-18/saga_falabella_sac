

class Detalle_Inventario:
    def __init__(self, cantidad):
        self.__cantidad = cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def get_cantidad(self):
        return self.__cantidad
