
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange, ValidationError, Optional

choices = ["EUR", "BTC", "ETH", "USDT", "ADA", "SOL", "XRP", "DOT", "DODGE", "SHIB"]

class MovimientoForm(FlaskForm):
    moneda_from = SelectField("Origen", choices=choices, validators=[DataRequired("Debe informar una divisa de origen")])
    cantidad_from = FloatField("Cantidad", 
                                    validators=[DataRequired("Debe informar una cantidad"), NumberRange(message="Debe ser una cantidad positiva", min=0.01)])
    moneda_to = SelectField("Destino", choices=choices, validators=[DataRequired("Debe informar una divisa de origen")])
    cantidad_to = FloatField("Cantidad", validators=[Optional()])
    cantidad_toH = HiddenField()
    
    calcular = SubmitField("Calcular")
    submit = SubmitField("Aceptar")

    def validate_cantidad_to(form, campo):
            if campo.data and campo.data < 0.01:
                raise ValidationError("Debe ser una cantidad positiva")    