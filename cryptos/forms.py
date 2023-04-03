
from flask_wtf import FlaskForm
from wtforms import DateField,TimeField,DecimalField,HiddenField,RadioField,StringField,SubmitField
from wtforms.validators import DataRequired

class MovimientoForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha')
    hora = TimeField('Hora')
    moneda_from = StringField('From', validators=[DataRequired()])
    cantidad_from = DecimalField('Q', places=2, validators=[DataRequired()])
    moneda_to = StringField('To', validators=[DataRequired()])
    cantidad_to = DecimalField('Q', places=2, validators=[DataRequired()])

    submit = SubmitField('Guardar')