from DataService.IDataService import IDataService
from Model.CustomWeatherData import CustomWeatherData
import redis
import json
from collections import namedtuple
from json import JSONEncoder

class RedisDataService(IDataService):

    def __init__(self) -> None:
        super().__init__()
        self.redis_host = "localhost"
        self.redis_port = 6379
        self.redis_password = ""
        # return redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)

    def SetData(self, key: str, data: CustomWeatherData):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            jsonData = json.dumps(data.__dict__)
            r.set(key, jsonData)
        except Exception as e:
            print(e)   
    
    def GetData(self, key: str):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            data = json.loads(r.get(key)) 
            return data 
        except Exception as e:
            print(e)
