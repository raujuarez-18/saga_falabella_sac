from model.Persona import Persona
class Cliente(Persona):
    def __init__(self, nombre, apellido, nro_identificacion, genero, celular, direccion, email_personal, RUC):
        super().__init__(nombre, apellido, nro_identificacion, genero, celular, direccion, email_personal)
        self.__RUC = RUC
        
    def set_RUC(self, RUC):
        self.__RUC = RUC
    
    def get_RUC(self):
        return self.__RUC
    
    