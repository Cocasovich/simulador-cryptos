import os

from flask import render_template

from . import app
from .models import DBManager

RUTA =  os.path.join('cryptos/data','simulador-cryptos.db')

@app.route('/')
def inicio():
    db = DBManager(RUTA)
    consulta = 'SELECT id, fecha, hora, moneda_from , cantidad_from, moneda_to, cantidad_to,precio_unitario FROM movimientos'
    movimientos = db.consultaSQL(consulta)
    return render_template("inicio.html", movs=movimientos)

@app.route('/compra')
def compra():
    return render_template("compra.html")

@app.route('/estado')
def estado():
    return "Estado de la inversión"

