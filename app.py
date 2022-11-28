
import requests
from datetime import datetime
import helpers
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def today():
    todayWeather = helpers.getWeatherData()
    rise = todayWeather["sys"]["sunrise"]  
    set = todayWeather["sys"]["sunset"]
    name = todayWeather["name"]
    page = "today"
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
    sunrise = helpers.time_converter(rise)
    sunset = helpers.time_converter(set)
    temp_max = round(todayWeather["main"]["temp_max"])
    temp_min = round(todayWeather["main"]["temp_min"])
    

    return render_template("index.html", page = page, name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)


@app.route('/5day')
def fiveDay():
    forecast = helpers.getForecastData()
    todayWeather = helpers.getWeatherData()
    fiveDayForecast = []
    for forecastItem in forecast["list"]:
        if helpers.isMidDay(forecastItem):
            fiveDayForecast.append(helpers.addPrettyFormat(forecastItem))
              
    
    # fiveDayForecast = [helpers.addPrettyFormat(day) 
    #                    for day in forecast["list"] 
    #                    if helpers.isMidDay(day)]
    
    
    name = forecast["city"]["name"]
    page = "5day"
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
    
    icon0 = forecast["list"][0]["weather"][0]["icon"]
   
    #         return day
 
    return render_template("fiveday.html", page = page, fiveDayForecast = fiveDayForecast, name=name,icon = icon, description = description,temp = temp)
    # return fiveDayForecast
    # return render_template("index.html", name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)

@app.route('/airpollution')
def airPollution():
    
   
    page = "airpollution"
    airPollution = helpers.getAirPollutionData()
    aqi = airPollution["list"][0]["main"]["aqi"]
    
    todayWeather = helpers.getWeatherData()
    name = todayWeather["name"]
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
   
  
    # return airPollution
    
    return render_template("airpollution.html", aqi = aqi,   page = page, name = name, icon = icon, description = description,temp = temp)


@app.route('/london')
def london():
    todayWeatherLon = helpers.getWeatherDataLondon()
    rise = todayWeatherLon["sys"]["sunrise"]  
    set = todayWeatherLon["sys"]["sunset"]
    name = todayWeatherLon["name"]
    page = "london"
    icon = f'http://openweathermap.org/img/wn/{todayWeatherLon["weather"][0]["icon"]}@2x.png'
    description = todayWeatherLon["weather"][0]["description"]
    temp = round(todayWeatherLon["main"]["temp"])
    sunrise = helpers.time_converter(rise)
    sunset = helpers.time_converter(set)
    temp_max = round(todayWeatherLon["main"]["temp_max"])
    temp_min = round(todayWeatherLon["main"]["temp_min"])
   

    return render_template("london.html", page = page, name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)

@app.route('/paris')
def paris():
    todayWeatherParis= helpers.getWeatherDataParis()
    rise = todayWeatherParis["sys"]["sunrise"]  
    set = todayWeatherParis["sys"]["sunset"]
    name = todayWeatherParis["name"]
    page = "paris"
    icon = f'http://openweathermap.org/img/wn/{todayWeatherParis["weather"][0]["icon"]}@2x.png'
    description = todayWeatherParis["weather"][0]["description"]
    temp = round(todayWeatherParis["main"]["temp"])
    sunrise = helpers.time_converter(rise)
    sunset = helpers.time_converter(set)
    temp_max = round(todayWeatherParis["main"]["temp_max"])
    temp_min = round(todayWeatherParis["main"]["temp_min"])
   

    return render_template("paris.html", page = page, name = name, icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)


if __name__ == '__main__':
    app.run(debug=True)