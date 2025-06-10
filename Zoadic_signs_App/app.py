from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    error = None
    zoadic = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'reset':
            return redirect(url_for('home'))
        elif action == 'show':
            try:
                month = int(request.form['month'])
                day = int(request.form['day'])
                datetime(year=2024, month=month, day=day)
            except(ValueError,KeyError):
                error = 'Invalid number'
            else:
                zoadic = determine_zoadic(month,day)

    return render_template('index.html', zoadic=zoadic, error=error)

def determine_zoadic(month,day):
    match month:
        case 1:
            if day<=19: zoadic = ('Capricorn')
            else: zoadic = ('Aquarius')
        case 2:
            if day<=18: zoadic = ('Aquarius')
            else: zoadic = ('Pisces')
        case 3:
            if day<=20: zoadic = ('Pisces')
            else: zoadic = ('Aries')
        case 4:
            if day<=19: zoadic = ('Aries')
            else: zoadic = ('Taurus')
        case 5:
            if day<=20: zoadic = ('Taurus')
            else: zoadic = ('Gemini')
        case 6:
            if day<=21: zoadic = ('Gemini')
            else: zoadic = ('Cancer')
        case 7:
            if day<=22: zoadic = ('Cancer')
            else: zoadic = ('Leo')
        case 8:
            if day<=22: zoadic = ('Leo')
            else: zoadic = ('Virgo')
        case 9:
            if day<=22: zoadic = ('Virgo')
            else: zoadic = ('Libra')
        case 10:
            if day<=23: zoadic = ('Libra')
            else: zoadic = ('Scorpio')
        case 11:
            if day<=21: zoadic = ('Scorpio')
            else: zoadic = ('Sagittarius')
        case 12:
            if day<=21: zoadic = ('Sagittarius')
            else: zoadic = ('Capricorn')
    return zoadic

if __name__ == '__main__':
    app.run(debug=True)