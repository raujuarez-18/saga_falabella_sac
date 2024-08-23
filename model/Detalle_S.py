class Detalle_Salida:
    def __init__(self, fecha, observaciones, cantidad):
        super().__init__(fecha, observaciones)
        self.__cantidad = cantidad
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def get_cantidad(self):
        return self.__cantidad
