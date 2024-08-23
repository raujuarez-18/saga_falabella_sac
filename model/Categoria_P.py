class Categoria_Producto:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def get_descripcion(self):
        return self.__descripcion