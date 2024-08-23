class Cargo_Laboral:
    def __init__(self, descripcion_e, salario_mensual):
        self.__descripcion_e = descripcion_e
        self.__salario_mensual = salario_mensual
    
    def set_descripcion(self, descripcion_e):
        self.__descripcion_e = descripcion_e
    def set_salario_mensual(self, salario_mensual):
        self.__salario_mensual = salario_mensual

    def get_descripcion_e(self):
        return self.__descripcion_e
    def get_salario_mensual(self):
        return self.__salario_mensual