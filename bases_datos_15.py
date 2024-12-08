import mysql.connector as mysql

"""
En este archivo usamos la Programacion Orientada a Objetos para gestionar la base de datos creada con el motor MySQL.
"""
class Basedatos():
    #metodo constructor para almacenar de entrada los datos que necesitamos para establecer conexion con la base de datos.
    def __init__(self,host,user,password,database) -> None:
        self.host = host
        self.user = user
        self.password = password
        #self.port = port
        self.database = database
        self.conexion = None
    #tenemos un metodo donde establecemos la conexion con la base de datos.
    def conectar(self):
        try:
            self.conexion = mysql.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                #port = self.port,
                database = self.database
            )
            print(f"status conexion: {self.conexion.is_connected()}")
        except:
            print("conexion fallida...")
    #metodo para insertar los datos pasados como tupla que ingreso el usuario.
    def insertar_datos(self,valores):
        #creamos un cursor.
        cursor = self.conexion.cursor()
        #ejecutamos el siguiente SQL.
        cursor.execute('INSERT INTO calculadora.operaciones(op,resultado) VALUES(%s,%s)', valores)
        #guardamos los datos.
        self.conexion.commit()
        #cerramos el cursor.
        cursor.close()


#creamos un diccionario con los datos de la conexion a la base de datos.
config_database = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'calculadora'
}
#creamos una instancia de la clase BaseDatos y le pasamos como parametro un kwargs.
objeto = Basedatos(**config_database)
#llamamos al metodo conectar para inicializar la conexion.
objeto.conectar()



