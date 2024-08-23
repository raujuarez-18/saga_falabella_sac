class Forma_Pago:
    def __init__(self, Tarjeta, efectivo, tras_ban):
        self.__Tarjeta = Tarjeta
        self.__efectivo = efectivo
        self.__tras_ban = tras_ban

    def set_Tarjeta(self, Tarjeta):
        self.__Tarjeta = Tarjeta
    def set_efectivo(self, efectivo):
        self.__efectivo = efectivo
    def set_tras_ban(self, tras_ban):
        self.__tras_ban = tras_ban
    
    def get_Tarjeta(self):
        return self.__Tarjeta
    def get_efectivo(self):
        return self.__efectivo
    def get_tras_ban(self):
        return self.__tras_ban