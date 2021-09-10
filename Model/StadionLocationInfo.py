class LocationInfo:
    def __init__(self, latitude: float, longitute: float, stadionName: str):
        self.latitude = latitude
        self.longitute = longitute
        self.stadionName = stadionName

stadionLocationMap = {
   "Partizan": LocationInfo(44.7885, 20.4585, "JNA"),
   "Barselona": LocationInfo(41.380898, 2.122820, "Camp Nou")
   }