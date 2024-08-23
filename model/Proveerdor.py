class Proveerdor:
    def __init__(self, nombre_p, direccion_p, telefono_p, email_p):
        self.__nombre_p = nombre_p
        self.__direccion_p = direccion_p
        self.__telefono_p = telefono_p
        self.__email_p = email_p

    def set_nombre_p(self, nombre_p):
        self.__nombre_p = nombre_p
    def set_direccion_p(self, direccion_p):
        self.__direccion_p = direccion_p
    def set_telefono_p(self, telefono_p):
        self.__telefono_p = telefono_p
    def set_email_p(self, email_p):
        self.__email_p = email_p

    def get_nombre_p(self):
        return self.__nombre_p
    def get_direccion_p(self):
        return self.__direccion_p
    def get_telefono_p(self):
        return self.__telefono_p
    def get_email_p(self):
        return self.__email_p