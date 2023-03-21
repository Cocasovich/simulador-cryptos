from flask import Flask

app = Flask(__name__)

@app.route('/')
def movements():
    return "Lista de movimientos"

@app.route('/purchase')
def purchase():
    return "Compra-venta e intercambio de cryptos y euros"

@app.route('/status')
def status():
    return "Estado de la inversión"
