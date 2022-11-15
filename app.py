
import requests 
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/city')
def search_city():
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    # city = request.args.get('q')  # city name passed as argument
    lat = 55.95
    lon = -3.18
    
    print("Calling API:")

    # call API and convert response into Python dictionary
    url = "https://api.openweathermap.org/data/2.5/weather?lat=55.95&lon=-03.18&appid=76e279b59efb88310df280e9c8142315&units=metric"
    
    apiReq = requests.get(url)
    
    data = apiReq.json()
    def time_converter(unix):
        return datetime.utcfromtimestamp(unix).strftime(' %H:%M:%S')
    rise = data["sys"]["sunrise"]  
    set = data["sys"]["sunset"]
    name = data["name"]
    icon = data["weather"][0]["icon"]
    description = data["weather"][0]["description"]
    temp = round(data["main"]["temp"])
    sunrise = time_converter(rise)
    sunset = time_converter(set)
    temp_max = round(data["main"]["temp_max"])
    temp_min = round(data["main"]["temp_min"])
    
    
    # return data
    
    return render_template("index.html", name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)

    # # error like unknown city name, inavalid api key
    # if response.get('cod') != 200:
    #     message = response.get('message', '')
    #     return f'Error getting temperature for {city.title()}. Error message = {message}'

    # # get current temperature and convert it into Celsius
    # current_temperature = response.get('main', {}).get('temp')
    # if current_temperature:
    #     current_temperature_celsius = round(current_temperature - 273.15, 2)
    #     return f'Current temperature of {city.title()} is {current_temperature_celsius} &#8451;'
    # else:
    #     return f'Error getting temperature for {city.title()}'


@app.route('/')
def index():
 
    return '<h1>Weather</h1>'


if __name__ == '__main__':
    app.run(debug=True)