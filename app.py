
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
    
    return render_template("index.html", page = page, name = name, lowerName = name.lower(), icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)


@app.route('/5day-edinburgh')
def fiveDayEdinburgh():
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
 
    return render_template("fiveday.html", page = page, fiveDayForecast = fiveDayForecast, name=name, lowerName = name.lower(),icon = icon, description = description,temp = temp)
    
    
@app.route('/airpollution-edinburgh')
def airPollutionEdinburgh():
    page = "airpollution"
    airPollution = helpers.getAirPollutionData()
    aqi = helpers.AQI[airPollution["list"][0]["main"]["aqi"]]
    aqic = helpers.AQIC[airPollution["list"][0]["main"]["aqi"]]
    aqid = helpers.AQID[airPollution["list"][0]["main"]["aqi"]]
    todayWeather = helpers.getWeatherData()
    name = todayWeather["name"]
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
    
    return render_template("airpollution.html", aqi = aqi, aqic = aqic, aqid = aqid, page = page, name = name, lowerName = name.lower(), icon = icon, description = description,temp = temp)


@app.route('/london')
def london():
    todayWeatherLon = helpers.getWeatherDataLondon()
    rise = todayWeatherLon["sys"]["sunrise"]  
    set = todayWeatherLon["sys"]["sunset"]
    name = todayWeatherLon["name"]
    page = "today"
    icon = f'http://openweathermap.org/img/wn/{todayWeatherLon["weather"][0]["icon"]}@2x.png'
    description = todayWeatherLon["weather"][0]["description"]
    temp = round(todayWeatherLon["main"]["temp"])
    sunrise = helpers.time_converter(rise)
    sunset = helpers.time_converter(set)
    temp_max = round(todayWeatherLon["main"]["temp_max"])
    temp_min = round(todayWeatherLon["main"]["temp_min"])

    return render_template("london.html", page = page, name = name, lowerName = name.lower(), icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)


@app.route('/5day-london')
def fiveDayLondon():
    forecast = helpers.getForecastDataLondon()
    todayWeather = helpers.getWeatherDataLondon()
    fiveDayForecast = []
    for forecastItem in forecast["list"]:
        if helpers.isMidDay(forecastItem):
            fiveDayForecast.append(helpers.addPrettyFormat(forecastItem))
    
    name = forecast["city"]["name"]
    page = "5day"
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
 
    return render_template("fiveday.html", page = page, fiveDayForecast = fiveDayForecast, name=name, lowerName = name.lower(),icon = icon, description = description,temp = temp)
    
    
@app.route('/airpollution-london')
def airPollutionLondon():

    page = "airpollution"
    airPollution = helpers.getAirPollutionDataLondon()
    aqi = helpers.AQI[airPollution["list"][0]["main"]["aqi"]]
    aqic = helpers.AQIC[airPollution["list"][0]["main"]["aqi"]]
    aqid = helpers.AQID[airPollution["list"][0]["main"]["aqi"]]
    todayWeather = helpers.getWeatherDataLondon()
    name = todayWeather["name"]
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
    
    return render_template("airpollution.html", aqi = aqi, aqic = aqic, aqid = aqid, page = page, name = name, lowerName = name.lower(), icon = icon, description = description,temp = temp)


@app.route('/paris')
def paris():
    todayWeatherParis= helpers.getWeatherDataParis()
    rise = todayWeatherParis["sys"]["sunrise"]  
    set = todayWeatherParis["sys"]["sunset"]
    name = todayWeatherParis["name"]
    page = "today"
    icon = f'http://openweathermap.org/img/wn/{todayWeatherParis["weather"][0]["icon"]}@2x.png'
    description = todayWeatherParis["weather"][0]["description"]
    temp = round(todayWeatherParis["main"]["temp"])
    sunrise = helpers.time_converter(rise)
    sunset = helpers.time_converter(set)
    temp_max = round(todayWeatherParis["main"]["temp_max"])
    temp_min = round(todayWeatherParis["main"]["temp_min"])

    return render_template("paris.html", page = page, name = name, lowerName = name.lower(), icon = icon, description = description,temp = temp, sunrise = sunrise, sunset = sunset, temp_max = temp_max, temp_min = temp_min)


@app.route('/5day-paris')
def fiveDayParis():
    forecast = helpers.getForecastDataParis()
    todayWeather = helpers.getWeatherDataParis()
    fiveDayForecast = []
    for forecastItem in forecast["list"]:
        if helpers.isMidDay(forecastItem):
            fiveDayForecast.append(helpers.addPrettyFormat(forecastItem))
            
    name = forecast["city"]["name"]
    page = "5day"
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
 
    return render_template("fiveday.html", page = page, fiveDayForecast = fiveDayForecast, name=name, lowerName = name.lower(),icon = icon, description = description,temp = temp)
 
 
@app.route('/airpollution-paris')
def airPollutionParis():
    page = "airpollution"
    airPollution = helpers.getAirPollutionDataParis()
    aqi = helpers.AQI[airPollution["list"][0]["main"]["aqi"]]
    aqic = helpers.AQIC[airPollution["list"][0]["main"]["aqi"]]
    aqid = helpers.AQID[airPollution["list"][0]["main"]["aqi"]]
    todayWeather = helpers.getWeatherDataParis()
    name = todayWeather["name"]
    icon = f'http://openweathermap.org/img/wn/{todayWeather["weather"][0]["icon"]}@2x.png'
    description = todayWeather["weather"][0]["description"]
    temp = round(todayWeather["main"]["temp"])
    
    return render_template("airpollution.html", aqi = aqi, aqic = aqic, aqid = aqid, page = page, name = name, lowerName = name.lower(), icon = icon, description = description,temp = temp)   
    
    
if __name__ == '__main__':
    app.run(debug=True)