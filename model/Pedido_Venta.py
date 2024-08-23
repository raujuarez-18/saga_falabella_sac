class Pedido_Venta:
    def __init__(self,fecha, total):
        self.__fecha = fecha
        self.__total = total

    def set_fecha(self, fecha):
        self.__fecha = fecha
    def set_total(self, total):
        self.__total = total

    def get_fecha(self):
        return self.__fecha
    def get_total(self):
        return self.__total