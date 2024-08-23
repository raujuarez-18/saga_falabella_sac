
class Usuario:
    def __init__(self, user_name, password, tipo_usuario):
        self.__user_name = user_name
        self.__password = password
        self.__tipo_usuario = tipo_usuario

    def set_user_name(self, user_name):
        self.__user_name = user_name
    def set_password(self, password):
        self.__password = password
    def set_tipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario

    
    def get_user_name(self):
        return self.__user_name
    def get_password(self):
        return self.__password
    def get_tipo_usuario(self):
        return self.__tipo_usuario