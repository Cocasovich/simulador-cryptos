from flask import Flask

RUTA_FICHERO = "cryptos/data/movimientos.csv"

# instanciamos Flask y le pasamos un nombre para la aplicación

app = Flask(__name__)

