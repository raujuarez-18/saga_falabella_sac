

class Jornada_Laboral:
    def __init__(self,  hora_en, hora_sa):
        self.__hora_en = hora_en
        self.__hora_sa = hora_sa
    
    def set_hora_en(self, hora_en):
        self.__hora_en = hora_en
    def set_hora_sa(self, hora_sa):
        self.__hora_sa = hora_sa
    
    def get_hora_en(self):
        return self.__hora_en
    def get_hora_sa(self):
        return self.__hora_sa