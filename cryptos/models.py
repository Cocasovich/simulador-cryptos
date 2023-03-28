from datetime import date

import sqlite3

class DBManager:
    
    def __init__(self, ruta):

        self.ruta = ruta

    def consultaSQL(self,consulta):

        # Conectar la base de datos
        conexion = sqlite3.connect(self.ruta)

        # Abrir un cursor
        cursor = conexion.cursor()

        # Ejecutar la consulta SQL sobre ese cursor
        cursor.execute(consulta)

        # Tratar los datos
            # Obetener los datos
        datos = cursor.fetchall()

        movimientos = []
        nombres_columna = []
        for columna in cursor.description:
            nombres_columna.append(columna[0])
        

        for dato in datos:
            indice = 0
            movimiento = {}
            for nombre in nombres_columna:
                movimiento[nombre] = dato[indice]
                indice += 1

            movimientos.append(movimiento)

            # Cerrar la conexión
        conexion.close()

            # Devolver la colección de resultados
        return movimientos


       
       