class Guia_de_movimiento:
    def __init__(self, fecha, observaciones):
        self.__fecha = fecha
        self.__observaciones = observaciones

    def set_fecha(self, fecha):
        self.__fecha = fecha
    def set_observaciones(self,observaciones):
        self.__observaciones = observaciones
    
    def get_fecha(self):
        return self.__fecha
    def get_observaciones(self):
        return self.__observaciones