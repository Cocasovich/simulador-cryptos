from datetime import date

import sqlite3

class DBManager:
    
    def __init__(self, ruta):

        self.ruta = ruta

    def consultaSQL(self,consulta):

        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)
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

        conexion.close()

        return movimientos


       
       