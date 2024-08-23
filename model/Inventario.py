

class Inventario:
    def __init__(self, observaciones_g_e, descripcion_i, stock_ini, stock_actual):
        self.__descripcion_i = descripcion_i
        self.__stock_ini = stock_ini
        self.__stock_actual = stock_actual

    def set_descripcion_i(self, descripcion_i):
        self.__descripcion_i = descripcion_i
    def set_stock_ini(self, stock_ini):
        self.__stock_ini = stock_ini
    def set_stock_actual(self, stock_actual):
        self.__stock_actual = stock_actual

    def get_descripcion_i(self):
        return self.__descripcion_i
    def get_stock_ini(self):
        return self.__stock_ini
    def get_stock_actual(self):
        return self.__stock_actual 