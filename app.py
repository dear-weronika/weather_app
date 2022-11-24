
import requests
from datetime import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def today():
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    # city = request.args.get('q')  # city name passed as argument
    lat = 55.95
    lon = -3.18
    
    print("Calling API:")

    # call API and convert response into Python dictionary
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=76e279b59efb88310df280e9c8142315&units=metric'
    
    apiReq = requests.get(url)
    
    data = apiReq.json()
    def time_converter(unix):
        return datetime.utcfromtimestamp(unix).strftime(' %H:%M')
    rise = data["sys"]["sunrise"]  
    set = data["sys"]["sunset"]
    name = data["name"]
    icon = f'http://openweathermap.org/img/wn/{data["weather"][0]["icon"]}@2x.png'
    description = data["weather"][0]["description"]
    temp = round(data["main"]["temp"])
    sunrise = time_converter(rise)
    sunset = time_converter(set)
    temp_max = round(data["main"]["temp_max"])
    temp_min = round(data["main"]["temp_min"])
    
    
    return render_template("index.html", name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)


@app.route('/5day')
def fiveDay():
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    # city = request.args.get('q')  # city name passed as argument
    lat = 55.95
    lon = -3.18
    
    print("Calling API:")

    # call API and convert response into Python dictionary
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=76e279b59efb88310df280e9c8142315&units=metric'
    
    apiReq = requests.get(url)
    # Change API format to Json
    data = apiReq.json()
 
    # Json -> Daytime -> string (hour)
    def midDay(day):
        return datetime.fromisoformat(day["dt_txt"]).strftime("%H")=="12"
    # filter elements from data["list"] list that dt_txt property is = 12
    fiveDayForecast = [d for d in data["list"] if midDay(d)]
    
    
    name = data["city"]["name"]
    icon0 = data["list"][0]["weather"][0]["icon"]
    # icon = f'http://openweathermap.org/img/wn/{data["weather"][0]["icon"]}@2x.png'
    description = data ["list"][0]["weather"][0]["description"]
    temp = round(data["list"][0]["main"]["temp"])
    #         return day
    
    return render_template("fiveday.html", fiveDayForecast = fiveDayForecast, name=name)
    # return fiveDayForecast
    # return render_template("index.html", name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)

@app.route('/alert')
def alert():
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    # city = request.args.get('q')  # city name passed as argument
    lat = 55.95
    lon = -3.18
    
    print("Calling API:")

    # call API and convert response into Python dictionary
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=76e279b59efb88310df280e9c8142315&units=metric'
    
    apiReq = requests.get(url)
    
    data = apiReq.json()
    def time_converter(unix):
        return datetime.utcfromtimestamp(unix).strftime(' %H:%M')
    rise = data["sys"]["sunrise"]  
    set = data["sys"]["sunset"]
    name = data["name"]
    icon = f'http://openweathermap.org/img/wn/{data["weather"][0]["icon"]}@2x.png'
    description = data["weather"][0]["description"]
    temp = round(data["main"]["temp"])
    sunrise = time_converter(rise)
    sunset = time_converter(set)
    temp_max = round(data["main"]["temp_max"])
    temp_min = round(data["main"]["temp_min"])
    
    
    return render_template("index.html", name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)


if __name__ == '__main__':
    app.run(debug=True)