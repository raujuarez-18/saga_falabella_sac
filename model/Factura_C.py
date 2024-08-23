from model.Documento_Cont import Documento_Contable
class Factura_Compra(Documento_Contable):
    def __init__(self, fecha, IGV, subtotal, total, observaciones, tp_doc):
        super().__init__(fecha, IGV, subtotal, total, observaciones)
        self.__tp_doc = tp_doc

    def set_tp_doc(self, tp_doc):
        self.__tp_doc = tp_doc
    
    def get_tp_doc(self):
        return self.__tp_doc
    
