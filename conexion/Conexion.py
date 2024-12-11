import psycopg2
class Conexion:

    """Metodo contructor de tu perro
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinariadb user=postgres host=localhost password=15dediciembre")
        
        """getConexion

            retorna la instancia de la base de datos
        """
    def getConexion(self):
        return self.con 