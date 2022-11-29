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
    
AQI = ['', 'Good 🤪', 'Fair 😌', 'Modarate 😐', 'Poor 😵', 'Very Poor ☠️']
AQIC = ['','bg-success','bg-info','bg-secondary','bg-warning','bg-danger']
    
def getWeatherData():
   return getAPIdataEdinburgh('weather')

def getForecastData():
    return getAPIdataEdinburgh('forecast')

def getAirPollutionData():
    return getAPIdataEdinburgh('air_pollution')

def getWeatherDataLondon():
   return getAPIdataLondon('weather')

def getForecastDataLondon():
    return getAPIdataLondon('forecast')

def getAirPollutionDataLondon():
    return getAPIdataLondon('air_pollution')

def getWeatherDataParis():
   return getAPIdataParis('weather')

def getForecastDataParis():
    return getAPIdataParis('forecast')

def getAirPollutionDataParis():
    return getAPIdataParis('air_pollution')

    
def getAPIdataEdinburgh(whatdata):
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    lat = 55.95
    lon = -3.18
    print("Calling API:")
    # call API and convert response into Python dictionary
    url = f'https://api.openweathermap.org/data/2.5/{whatdata}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    apiReq = requests.get(url)
    
    return  apiReq.json()

def getAPIdataLondon(whatdata):
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    lat = 51.509865
    lon = -0.118092
    print("Calling API:")
    # call API and convert response into Python dictionary
    url = f'https://api.openweathermap.org/data/2.5/{whatdata}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    apiReq = requests.get(url)
    
    return  apiReq.json()

def getAPIdataParis(whatdata):
    API_KEY = '76e279b59efb88310df280e9c8142315' # initialize your key here
    lat = 48.85
    lon = 2.35
    print("Calling API:")
    # call API and convert response into Python dictionary
    url = f'https://api.openweathermap.org/data/2.5/{whatdata}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    apiReq = requests.get(url)
    
    return  apiReq.json()

