from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city_name = request.args.get('city')
    weather_data = get_weather_forecast(city_name)
    return render_template('weather.html', city=city_name, weather_data=weather_data)

def get_weather_forecast(city):
    api_key = '361c92dfc282a3e0ca31ecaab6487059'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    

    if response.status_code == 200:
        weather_data = response.json()

        return weather_data
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)