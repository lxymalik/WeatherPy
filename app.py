from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)
    print(weather_data)
    if weather_data['cod'] != 200:
        render_template('no_data.html')

    weather = {
        'title': weather_data['name'],
        'description': weather_data['weather'][0]['description'],
        'temp': weather_data['main']['temp'],
        'feels_like': weather_data['main']['feels_like'],
    }
    return render_template('weather.html', weather = weather)

if __name__ == '__main__':
    serve(app, listen='*:8080')