
from flask_wtf import FlaskForm
from wtforms import DateField,TimeField,DecimalField,HiddenField,RadioField,StringField,SubmitField

class MovimientoForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha')
    hora = TimeField('Hora')
    moneda_from = StringField('From')
    cantidad_from = DecimalField('Q', places=2)
    moneda_to = StringField('To')
    cantidad_to = DecimalField('Q', places=2)

    submit = SubmitField('Guardar')