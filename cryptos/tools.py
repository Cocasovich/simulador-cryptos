
def cantidad_disponible(moneda, movimientos):
    total = 0
    for fila in movimientos:
        if fila["moneda_to"] == moneda:
            total = fila["cantidad_to"] + total
        if fila["moneda_from"] == moneda:
            total = total - fila["cantidad_from"]
    return total