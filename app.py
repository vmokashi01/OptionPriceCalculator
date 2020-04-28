from black_scholes import *
from flask import *
from form import *
from option_con import *
from data_collection import is_valid
from werkzeug.datastructures import MultiDict

app = Flask(__name__, template_folder = "templates")
app.secret_key = 'test'

@app.route('/', methods = ('GET', 'POST'))
def start():
    form = TickerForm(csrf_enabled=False)
    if form.validate_on_submit():
        if is_valid(form.ticker.data):
            session['ticker'] = form.ticker.data.upper()
        else:
            session['ticker'] = ""
        return redirect('/index')

    return render_template('/start.html', title = "Calculator Start", description = "Enter the ticker", form = form)

@app.route('/index', methods = ('GET','POST'))
def index():
    if session.get('ticker', None) == "":
        #print("a")
        form = CalculatorParamsForm(csrf_enabled=False)
        if form.validate_on_submit():
            print(form.data)
            session['option'] = Option(form.option_type.data, form.stock_price.data, form.strike_price.data, form.risk_free.data, form.vol.data, form.time_expiry.data).toJson()
            return redirect(url_for('output'))
    else:
        #print("b")
        form = CalculatorParamsForm(csrf_enabled=False, data=MultiDict({'stock_price': float(get_price(session.get('ticker', None))), 'vol': float(get_vol(session.get('ticker', None)))}))
        if form.is_submitted(): #if form.validate_on_submit():
            print(form.data)
            session['option'] = Option(form.option_type.data, form.stock_price.data, form.strike_price.data, form.risk_free.data, form.vol.data, form.time_expiry.data).toJson()
            return redirect(url_for('output'))

    return render_template('/index.html', title = "Options Price Calculator", description = "Calculates the price of options using Black-Scholes.", form = form)


#ADD ERRORS from incorrect input values

@app.route('/output')
def output():
    option = json.loads(session.get('option', None))
    if option["con_type"] == 'European Call':
        price = black_scholes_call(option["stock_price"], option["strike_price"], option["risk_free_rate"], option["volatility"], option["time"])
    elif option['con_type'] == 'European Put':
        price = black_scholes_put(option["stock_price"], option["strike_price"], option["risk_free_rate"], option["volatility"], option["time"])
    return render_template('/output.html', title = "Calculated Price", description = "Calculator output.", price = price)

if __name__ == "__main__":
    app.run(debug=True)