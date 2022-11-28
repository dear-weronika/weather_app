import requests
from datetime import datetime
def time_converter(unix):
        return datetime.utcfromtimestamp(unix).strftime('%H:%M')
    
def isMidDay(day):
        return datetime.fromisoformat(day["dt_txt"]).strftime("%H")=="12"
    # filter elements from data["list"] list that dt_txt property is = 12
def addPrettyFormat(day_dict):
        day_dict["dayOfWeek"]= datetime.fromisoformat(day_dict["dt_txt"]).strftime("%A")
        day_dict["tempToShow"]= str(round(day_dict["main"]["temp"]))+ "°C"
        return day_dict
    
def getWeatherData():
   return getAPIdata('weather')

def getForecastData():
    return getAPIdata('forecast')

def getAirPollutionData():
    return getAPIdata('air_pollution')

    
def getAPIdata(whatdata):
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    # city = request.args.get('q')  # city name passed as argument
    lat = 55.95
    lon = -3.18
    print("Calling API:")
    # call API and convert response into Python dictionary
    url = f'https://api.openweathermap.org/data/2.5/{whatdata}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    apiReq = requests.get(url)
    
    return  apiReq.json()

