
from flask_wtf import FlaskForm, CsrfProtect
from wtforms import TextField, FloatField, SelectField, SubmitField, StringField
from wtforms.validators import DataRequired
from data_collection import *

class CalculatorParamsForm(FlaskForm):
    
    option_type = SelectField('Option Type: ', [DataRequired()], choices=[("European Call", "Call"), ("European Put", "Put")])
    stock_price = FloatField('Stock Price: ', [DataRequired()]) #default = get_price(session.get("ticker", None))
    strike_price = FloatField('Strike Price: ', [DataRequired()])
    risk_free = FloatField('Risk-free Interest Rate (Default 10-Year US Treasury Bond): ', [DataRequired()], default = get_risk_free())
    vol = FloatField('Volatility: ', [DataRequired()]) #default = get_vol(session.get("ticker", None))
    time_expiry = FloatField('Time to Expiry (Years): ', [DataRequired()]) #add default
    submit = SubmitField('Calculate Price')

class TickerForm(FlaskForm):
    ticker = StringField('Enter a ticker (optional): ')
    submit = SubmitField('Next Step')