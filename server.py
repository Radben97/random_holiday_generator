from flask import Flask,render_template,request
from holiday import Get_Holiday
from waitress import serve
from random import randint
app = Flask(__name__)
@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')
@app.route('/holiday')
def Get_holiday():
    try:
        country = request.args.get('country')
        if not country.strip():
            country = "India"
        holiday_data = Get_Holiday(country)
        random_number = randint(0,len(holiday_data)-1)
        return render_template (
            "holiday.html",
            title=holiday_data[random_number]['country'],
            date=holiday_data[random_number]['date'],
            holidays=holiday_data[random_number]['name']
        )
    except Exception:
        return f"Invalid country: Enter a valid country name"
if __name__ == "__main__":
    serve(app,host="0.0.0.0",port="8000")