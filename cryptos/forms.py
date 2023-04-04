
from flask_wtf import FlaskForm
from wtforms import DateField,TimeField,DecimalField,HiddenField,RadioField,StringField,SubmitField
from wtforms.validators import DataRequired

class MovimientoForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha', validators = [DataRequired(message="Debes introducir una fecha")])
    hora = TimeField('Hora', validators=[DataRequired(message="Debes introducir la hora")])
    moneda_from = StringField('From', validators=[DataRequired(message="Debes especificar una divisa")])
    cantidad_from = DecimalField('Q', places=2, validators=[DataRequired(message="La cantidad debe tener un valor")])
    moneda_to = StringField('To', validators=[DataRequired(message="Debes especificar una divisa")])
    cantidad_to = DecimalField('Q', places=2, validators=[DataRequired(message="La cantidad debe tener un valor")])

    submit = SubmitField('Guardar')