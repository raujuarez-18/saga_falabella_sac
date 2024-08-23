
class Detalle_Pedido:
    def __init__(self,pedido, cantidad):
        self.__pedido = pedido
        self.__cantidad = cantidad
    
    def set_pedido(self, pedido):
        self.__pedido = pedido
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_pedido(self):
        return self.__pedido
    def get_cantidad_v(self):
        return self.__cantidad