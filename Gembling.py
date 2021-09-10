from DataService.RedisDataService import RedisDataService
from DataService.IDataService import IDataService
from BusinessLogic.OpenWeatherProcessWeatherData import OpenWeatherProcessWeatherData
from BusinessLogic.ProcessWeatherData import ProcessWeatherData
from Model.StadionLocationInfo import stadionLocationMap

def ProcessWeatherDataFactory() -> ProcessWeatherData:
    """
    Factory method that return appropriate implementation of abstract class 

    Returns
        IProcessWeatherData: implementation of ProcessWeatherData abstract class
    """    
    return OpenWeatherProcessWeatherData()

def DataServiceFactory() -> IDataService:
    """
    Factory method that return appropriate implementation of interface 

    Returns
        IDataService: implementation of IDataService interface
    """   
    return RedisDataService()

processWeatherData = ProcessWeatherDataFactory()
dataService = DataServiceFactory()

# 1. next step: on booking api find match that start in for example next 5 minutes(custom setting)
# 2. find domestic team in stadionLocationMap dictonary and start processing
for key in stadionLocationMap:
    data = processWeatherData.GetData(key)
    # save data to storage
    dataService.SetData(key, data)
    processWeatherData.ProcessData(data)
