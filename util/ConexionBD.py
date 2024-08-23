import mysql.connector

class ConexionBd:
    
    def __init__(self) -> None:
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='bd_saga_falabella',
                                                user='root',
                                                password='alex')
    
    def getConexionBD(self):
        return self.conexion