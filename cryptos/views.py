import os

from flask import redirect, render_template, request, url_for

from . import app
from .forms import MovimientoForm
from .models import DBManager

RUTA =  os.path.join('cryptos/data','simulador-cryptos.db')

@app.route('/')
def home():
    db = DBManager(RUTA)
    consulta = 'SELECT id, fecha, hora, moneda_from , cantidad_from, moneda_to, cantidad_to,precio_unitario FROM movimientos'
    movimientos = db.consultaSQL(consulta)
    return render_template("inicio.html", movs=movimientos)

@app.route('/nuevo', methods=['GET', 'POST'])
def new_movement():

    if request.method == 'GET':
        formulario = MovimientoForm()
        return render_template('form_movimiento.html', form=formulario)
    
    if request.method == 'POST':
        datos = request.form
        return redirect(url_for('home'))


@app.route('/estado')
def state():
    return "Estado de la inversion"

