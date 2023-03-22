from flask import render_template

from . import app

from .models import ListaMovimientos

# mediante un decorador asignamos una ruta (path) de la URL
# a la función que debe ejecutarse cuando se recibe una petición 
# con esa ruta

@app.route('/')
def movements():
    lista = ListaMovimientos()
    lista.leer_desde_archivo()

    return render_template("inicio.html", movs = lista.lista_movimientos )

@app.route('/purchase')
def purchase():
    return "Compra-venta e intercambio de cryptos y euros"

@app.route('/status')
def status():
    return "Estado de la inversión"

