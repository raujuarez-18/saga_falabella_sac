from model.Documento_Cont import Documento_Contable
class Doc_Venta(Documento_Contable):
    def __init__(self, fecha, IGV, subtotal, total, observaciones,tipo_doc):
        super().__init__(fecha, IGV, subtotal, total, observaciones)
        self.__tipo_doc = tipo_doc

    def set_tipo_doc(self, tipo_doc):
        self.__tipo_doc = tipo_doc
    

    def get_tipo_doc(self):
        return self.__tipo_doc
    