class CustomWeatherData:

    def __init__(self):
        self.clubName = ""
        self.stadionName = ""
        self.temperature = 0
        self.isRain = False
        self.isSnow = False
    
    def __str__(self):
        return "Club name: {0} Stadion Name: {1} Temperature: {2} Is rain: {3} Is snow: {4}".format(self.clubName, self.stadionName, self.temperature, self.isRain, self.isSnow)