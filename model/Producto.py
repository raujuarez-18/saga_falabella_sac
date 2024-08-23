
class Productos:
    def __init__(self,stock_max, stock_min, nombre, fecah_caducidad, estado):    
        self.__stock_max = stock_max
        self.__stock_min = stock_min
        self.__nombre = nombre
        self.__fecah_caducidad = fecah_caducidad
        self.__estado = estado
    
    def set_stock_max(self, stock_max):
        self.__stock_max = stock_max
    def set_stock_min(self, stock_min):
        self.__stock_min = stock_min
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_fecah_caducidad(self, fecah_caducidad):
        self.__fecah_caducidad = fecah_caducidad
    def set_estado(self, estado):
        self.__estado = estado

    def get_stock_max(self):
        return self.__stock_max
    def get_stock_min(self):
        return self.__stock_min
    def get_nombre(self):
        return self.__nombre
    def get_fecah_caducidad(self):
        return self.__fecah_caducidad
    def get_estado(self):
        return self.__estado