from model.Persona import Persona

class Empleado(Persona):

    def __init__(self, nombre, apellido, nro_identificacion, genero, celular, direccion, email_personal, fecha_ingreso):
        super().__init__(nombre, apellido, nro_identificacion, genero, celular, direccion, email_personal)
        self.__fecha_ingreso = fecha_ingreso

    def set_fecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso