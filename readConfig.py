from lib.ConvertJsonObject import ConvertJsonObject 

#defining the valid json filenames with path
file_valid1 = '.\\fixtures\\config.json'
file_valid2 = '.\\fixtures\\config.local.json'

#defining the invalid json filenames with path
file_invalid1 = '.\\fixtures\\config.invalid.json'
file_invalid2 = '.\\fixtures\\config.also_invalid.json'

myObj = ConvertJsonObject()

# calling invalid json file one
rc = myObj.convertJsonObjectToClass(file_invalid1)
if rc != None:
    print(rc.environment) 
    print(rc.database.username)
    print(rc.database.host) 
    print(rc.database.port) 


# calling valid json file one
rc = myObj.convertJsonObjectToClass(file_valid1)

if rc != None:
    print(rc.environment) 
    print(rc.database.username)
    print(rc.database.host) 
    print(rc.database.port) 

# calling valid json file two
rc = myObj.convertJsonObjectToClass(file_valid2)

if rc != None:
    print(rc.environment) 
    print(rc.database.username)
    print(rc.database.host) 
    print(rc.database.port) 
