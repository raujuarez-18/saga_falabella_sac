from model.Detalle_Com import Detalle_Comercial
class Detalle_Documento_Venta(Detalle_Comercial):
    def __init__(self, precio, cantidad):
        super().__init__(precio, cantidad)