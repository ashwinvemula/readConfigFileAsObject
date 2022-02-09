
from lib.CustomJsonObject import CustomJsonObject

file_valid1 = '.\\fixtures\\config.json'
file_valid2 = '.\\fixtures\\config.local.json'
file_invalid1 = '.\\fixtures\\config.invalid.json'
file_invalid2 = '.\\fixtures\\config.also_invalid.json'

myObj = CustomJsonObject()
rc = myObj.convertJsonObjectToClass(file_valid1)

if rc != None:
    print(rc.environment) 
    print(rc.database.username)
    print(rc.database.host) 
    print(rc.database.port) 
    print(rc.cache.redis)
