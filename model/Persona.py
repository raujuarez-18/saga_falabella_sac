class Persona:
    def __init__(self, nombre, apellido, nro_identificacion, genero, celular, direccion, email_personal):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nro_identificacion = nro_identificacion
        self.__genero = genero
        self.__celular = celular
        self.__direccion = direccion
        self.__email_personal = email_personal

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_apellido(self, apellido):
        self.__apellido = apellido
    def set_nro_identificacion(self, nro_identificacion):
        self.__nro_identificacion = nro_identificacion
    def set_genero(self, genero):
        self.__genero = genero
    def set_celular(self, celular):
        self.__celular = celular
    def set_direccion(self, direccion):
        self.__direccion = direccion
    def set_email_personal(self, email_personal):
        self.__email_personal = email_personal

    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_nro_identificacion(self):
        return self.__nro_identificacion
    def get_genero(self):
        return self.__genero
    def get_celular(self):
        return self.__celular
    def get_direccion(self):
        return self.__direccion
    def get_email_personal(self):
        return self.__email_personal

    
