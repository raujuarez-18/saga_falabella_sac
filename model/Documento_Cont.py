class Documento_Contable:
    def __init__(self, fecha, IGV, subtotal, total, observaciones):
        self.__fecha = fecha
        self.__IGV = IGV
        self.__subtotal = subtotal
        self.__total = total
        self.__observaciones = observaciones

    def set_fecha(self, fecha):
        self.__fecha = fecha
    def set_IGV(self, IGV):
        self.__IGV = IGV
    def set_subtotal(self, subtotal):
        self.__subtotal = subtotal
    def set_total(self, total):
        self.__total = total
    def set_observaciones(self, observaciones):
        self.__observaciones = observaciones
    
    def get_fecha(self):
        return self.__fecha
    def get_IGV(self):
        return self.__IGV
    def get_subtotal(self):
        return self.__subtotal
    def get_total(self):
        return self.__total
    def get_observaciones(self):
        return self.__observaciones