import csv

from . import RUTA_FICHERO

class Movimiento:
    def __init__(self, fecha, hora, divisa_1 , cantidad_1, divisa_2, cantidad_2, P_U ):
        self.fecha = fecha
        self.hora = hora
        self.divisa_1 = divisa_1
        self.cantidad_1 = cantidad_1
        self.divisa_2 = divisa_2
        self.cantidad_2 = cantidad_2
        self.P_U = P_U


class ListaMovimientos:
    """
    Almacenar ls lista con todos los movimientos
    """

    def __init__(self):
        self.lista_movimientos = []

    def leer_desde_archivo(self):
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                self.lista_movimientos.append(fila)