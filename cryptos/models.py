import csv

from datetime import date

from . import RUTA_FICHERO

class Movimiento:
    def __init__(self, fecha, hora, divisa_1 , cantidad_1, divisa_2, cantidad_2, P_U ):
        
        self.errores = []

        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            self.errores.append("El formato de la fecha no es válido")

        self.hora = hora
        self.divisa_1 = divisa_1
        self.cantidad_1 = cantidad_1
        self.divisa_2 = divisa_2
        self.cantidad_2 = cantidad_2
        self.P_U = P_U

    @property
    def has_errors(self):
        return len(self.errores) > 0
    
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
                mov = Movimiento(
                    fila["fecha"], 
                    fila["hora"], 
                    fila["divisa_1"], 
                    fila["cantidad_1"],
                    fila["divisa_2"],
                    fila["cantidad_2"],
                    fila["P_U"])
                self.lista_movimientos.append(mov)