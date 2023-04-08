from datetime import date

import requests
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

    def consultaConParametros(self, consulta, params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()

        resultado = False
        
        try:
            cursor.execute(consulta,params)
            conexion.commit()
            resultado = True

        except sqlite3.Error as e:
            print(f"Se ha producido este error al insertar: {e}")
            conexion.rollback

        conexion.close()

        return resultado
    


class APIException(Exception):
    pass

class APIManager:
    
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def calcular_tasa(self,moneda_from,cantidad_from,moneda_to):
        url = self.url.format(moneda_from, moneda_to,self.key)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tasa = data["rate"]

            total_cambio = tasa * cantidad_from
            return total_cambio
        
        raise APIException(f"{response.status_code} - {response.text}")