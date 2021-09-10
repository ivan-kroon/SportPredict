from Model.CustomWeatherData import CustomWeatherData
from abc import ABC, abstractmethod
from Model.CustomWeatherData import CustomWeatherData

class IDataService(ABC):

    @abstractmethod
    def SetData(self, key: str, data: CustomWeatherData):
        pass
    
    @abstractmethod
    def GetData(self, key: str) -> CustomWeatherData:
        pass