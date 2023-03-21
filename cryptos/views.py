from flask import render_template

from . import app

# mediante un decorador asignamos una ruta (path) de la URL
# a la función que debe ejecutarse cuando se recibe una petición 
# con esa ruta

@app.route('/')
def movements():
    return render_template("inicio.html")

@app.route('/purchase')
def purchase():
    return "Compra-venta e intercambio de cryptos y euros"

@app.route('/status')
def status():
    return "Estado de la inversión"

