import csv

from datetime import date

import sqlite3

# from . import RUTA_FICHERO

# class Movimiento:
#     def __init__(self, fecha, hora, moneda_from , cantidad_from,
#                   moneda_to, cantidad_to, P_U ):
        
#         self.errores = []

#         try:
#             self.fecha = date.fromisoformat(fecha)
#         except ValueError:
#             self.fecha = None
#             self.errores.append("El formato de la fecha no es válido")

#         self.hora = hora
#         self.moneda_from = moneda_from
#         self.cantidad_from = cantidad_from
#         self.moneda_to = moneda_to
#         self.cantidad_to = cantidad_to
#         self.P_U = P_U

#     @property
#     def has_errors(self):
#         return len(self.errores) > 0
    
# class ListaMovimientos:

#     def __init__(self):
#         self.lista_movimientos = []

#     def leer_desde_archivo(self):
#         with open(RUTA_FICHERO, 'r') as fichero:
#             reader = csv.DictReader(fichero)
#             for fila in reader:
#                 mov = Movimiento(
#                     fila["fecha"], 
#                     fila["hora"], 
#                     fila["moneda_from"], 
#                     fila["cantidad_from"],
#                     fila["moneda_to"],
#                     fila["cantidad_to"],
#                     fila["P_U"])
#                 self.lista_movimientos.append(mov)

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
        # nombres_columna = ['id','fecha','hora',
        #                    'moneda_from','cantidad_from',
        #                    'moneda_to','cantidad_to',
        #                    'precio_unitario']
        nombres_columna = []
        for columna in cursor.description:
            nombres_columna.append(columna[0])
        

        for dato in datos:
            # movimiento = {
            #     'id': dato[0],
            #     'fecha': dato[1],
            #     'moneda_from': dato[2],
            #     'cantidad_from': dato[3],
            #     'moneda_to': dato[4],
            #     'cantidad_from': dato[5],
            #     'moneda_from': dato[6],
            #     'P_U': dato[7]
            # }

            indice = 0
            movimiento ={}
            for nombre in nombres_columna:
                movimiento[nombre] = dato[indice]
                indice += 1

            movimientos.append(movimiento)

            # Cerrar la conexión
        conexion.close()

            # Devolver la colección de resultados
        return self.movimientos


       
       