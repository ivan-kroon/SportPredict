import requests
import json
from Model.StadionLocationInfo import stadionLocationMap
from BusinessLogic.ProcessWeatherData import ProcessWeatherData
from Model.CustomWeatherData import CustomWeatherData

class OpenWeatherProcessWeatherData(ProcessWeatherData):
    
    def GetData(self, key: str) -> CustomWeatherData:
        serviceUrl = "https://community-open-weather-map.p.rapidapi.com/find"
        headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "3d630c2769msh9736def547e34ccp1c3606jsn61a03739470f"
        }

        latitude = stadionLocationMap[key].latitude
        longitute = stadionLocationMap[key].longitute
        querystring = {f"lat": f"{latitude}", f"lon": f"{longitute}", "cnt":"1"}

        # "cnt":"1", "mode":"null","lon":"0","type":"link, accurate","lat":"0","units":"imperial, metric"

        response = requests.request("GET", serviceUrl, headers=headers, params=querystring)

        weatherData = json.loads(response.text)

        customWeatherData = CustomWeatherData()
        customWeatherData.clubName = key
        customWeatherData.stadionName = stadionLocationMap[key].stadionName
        customWeatherData.isRain = weatherData['list'][0]['rain'] != None
        customWeatherData.isSnow = weatherData['list'][0]['snow'] != None
        customWeatherData.temperature = weatherData['list'][0]['main']['temp']

        return customWeatherData

