import os
import sqlite3
import requests
import datetime
from flask import render_template, redirect, request, url_for, flash
from . import app
from .forms import MovimientoForm
from .models import DBManager, APIManager, APIException
from .tools import cantidad_disponible, saldo_euros_invertidos

RUTA = os.path.join('cryptos/data', 'simulador-cryptos.db')
db = DBManager(RUTA)
api_manager = APIManager(app.config.get(
    "COIN_API_URL"), app.config.get("API_KEY"))


@app.route('/')
def home():
    consulta = 'SELECT id, fecha, hora, moneda_from , cantidad_from, moneda_to, cantidad_to,precio_unitario FROM movimientos'
    movimientos = db.consultaSQL(consulta)
    return render_template("inicio.html", movs=movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def new_movement():

    if request.method == 'GET':
        formulario = MovimientoForm()
        return render_template('form_movimiento.html', form=formulario)

    else:
        formulario = MovimientoForm(data=request.form)
        if formulario.validate_on_submit():
            if formulario.data["calcular"]:

                if formulario.data.get("moneda_from") != 'EUR':
                    consulta = 'SELECT moneda_from, cantidad_from, moneda_to, cantidad_to FROM movimientos'
                    movimientos = db.consultaSQL(consulta)

                    total_disponible = cantidad_disponible(
                        formulario.data.get("moneda_from"), movimientos)
                    if total_disponible < formulario.data.get("cantidad_from"):

                        flash(
                            f"La cantidad de {formulario.data.get('moneda_from')} no es suficiente")
                        return render_template("form_movimiento.html", form=formulario)

                try:
                    cantidad_to = api_manager.calcular_tasa(formulario.data.get("moneda_from"),
                                                            formulario.data.get(
                                                                "cantidad_from"),
                                                            formulario.data.get("moneda_to"))

                except APIException as error:
                    print("Se ha producido un error al consultar la tasa:", error)
                    flash(
                        f"Se ha producido un error al consultar la tasa: {error}")
                    return render_template("form_movimiento.html", form=formulario)
                except requests.RequestException as error:
                    print("Se ha producido un error al consultar la tasa:", error)
                    flash(f"Se ha producido un error al consultar la tasa")
                    return render_template("form_movimiento.html", form=formulario)

                formulario.cantidad_to.data = cantidad_to
                formulario.cantidad_toH.data = cantidad_to

                return render_template('form_movimiento.html', form=formulario)

            elif formulario.data["submit"]:
                now = (datetime.datetime.now())
                fecha = now.strftime("%Y-%m-%d")
                hora = now.strftime("%H:%M:%S")
                cantidad_from = float(formulario.cantidad_from.data)
                cantidad_to = float(formulario.cantidad_toH.data)
                precio_unitario = cantidad_from/cantidad_to
                db.consultaConParametros("""INSERT INTO movimientos (fecha, hora, moneda_from,cantidad_from,moneda_to,cantidad_to,precio_unitario) VALUES (?,?,?,?,?,?,?)""",
                                         [fecha, hora, formulario.moneda_from.data,
                                          formulario.cantidad_from.data,
                                          formulario.moneda_to.data,
                                          float(formulario.cantidad_toH.data),
                                          precio_unitario])

                return redirect(url_for("home"))

        else:
            return render_template("form_movimiento.html", form=formulario)


@app.route('/estado')
def state():
    consulta = 'SELECT moneda_from, cantidad_from, moneda_to, cantidad_to FROM movimientos'
    movimientos = db.consultaSQL(consulta)

    cryptos = []
    for fila in movimientos:
        if fila["moneda_from"] != "EUR" and fila["moneda_from"] not in cryptos:
            cryptos.append(fila["moneda_from"])
        if fila["moneda_to"] != "EUR" and fila["moneda_to"] not in cryptos:
            cryptos.append(fila["moneda_to"])

    wallet = {}
    for crypto in cryptos:
        wallet[crypto] = cantidad_disponible(crypto, movimientos)

    total_cypto_a_euro = 0
    for clave, valor in wallet.items():

        valor_wallet_euros = api_manager.calcular_tasa(clave, valor, 'EUR')
        total_cypto_a_euro = round(valor_wallet_euros + total_cypto_a_euro, 2)

    total_from_euros, saldo = saldo_euros_invertidos(movimientos)

    total_inversion = total_from_euros + saldo + total_cypto_a_euro

    return render_template('estado.html', total_from_euros=f'{total_from_euros:.2f} €', 
                    saldo=f'{saldo:.2f} €', 
                    total_cypto_a_euro=f'{total_cypto_a_euro:.2f} €', 
                    total_inversion=f'{total_inversion:.2f} €')
