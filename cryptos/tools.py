
def cantidad_disponible(moneda, movimientos):
    total = 0
    for fila in movimientos:
        if fila["moneda_to"] == moneda:
            total = fila["cantidad_to"] + total
        if fila["moneda_from"] == moneda:
            total = total - fila["cantidad_from"]
    return total


def saldo_euros_invertidos(movimientos):
    total_to_euros = 0
    total_from_euros = 0
    for fila in movimientos:
        if fila["moneda_to"] == "EUR":
            total_to_euros += fila["cantidad_to"]
        if fila["moneda_from"] == "EUR":
            total_from_euros += fila["cantidad_from"]
    saldo = total_to_euros - total_from_euros
    return total_from_euros, saldo
