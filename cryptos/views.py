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
        db = DBManager(RUTA)
        formulario = MovimientoForm(data=request.form)
        if formulario.validate():

            cantidad_from = float(formulario.cantidad_from.data)
            cantidad_to = float(formulario.cantidad_to.data)
            precio_unitario = cantidad_from/cantidad_to

            params = (
                formulario.fecha.data.isoformat(),
                formulario.hora.data.isoformat(),
                formulario.moneda_from.data,
                cantidad_from,
                formulario.moneda_to.data,
                cantidad_to,
                precio_unitario
            )
            consulta = 'INSERT INTO movimientos (fecha, hora, moneda_from, cantidad_from, moneda_to, cantidad_to, precio_unitario) VALUES (?,?,?,?,?,?,?)'
            movimientos = db.consultaConParametros(consulta,params)
            if movimientos:
                return redirect(url_for('home'))
            return 'El movimiento no se ha podido guardar en la base de datos'
            
        else:
            return "El formulario tiene errores"

@app.route('/estado')
def state():
    return "Estado de la inversion"

