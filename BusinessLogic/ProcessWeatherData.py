from abc import ABC, abstractmethod
from Model.CustomWeatherData import CustomWeatherData

class ProcessWeatherData(ABC):

    @abstractmethod
    def GetData(self, key: str) -> CustomWeatherData:
        """
        Getting data from weather web service and parse it in custom class for future processing

        Returns
            CustomWeatherData: custom class for future processing
        """
        pass
    
    def ProcessData(self, data: CustomWeatherData):
        """
        Process parsed weather data

        Args
            data (CustomWeatherData): data to be processed
        Returns
            str: Depends on the data values
        """
        print("PROCESSING INFO: {0}".format(data.__str__()))

        if data.isRain or data.isSnow:
            print("It is rain or snow!")
            print("Start processing data...")
            print(data)
            print("Finished processing data...")
        else:
            print("There is no rain or snow in this moment, proccesing skipped!")


