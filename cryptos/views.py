import os

from flask import render_template

from . import app
from .models import DBManager

@app.route('/')
def inicio():
    ruta = os.path.join('data','simulador-cryptos.db')
    db = DBManager
    consulta = 'SELECT id, fecha, hora, moneda_from , cantidad_from, moneda_to, cantidad_to,P_U FROM movimientos'
    movimientos = db.consultaSQL(consulta)
    return render_template("inicio.html", movs=movimientos)

@app.route('/compra')
def compra():
    return render_template("compra.html")

@app.route('/estado')
def estado():
    return "Estado de la inversión"

