import json

from lib.DynamicClass import DynamicClass


class ConvertJsonObject:
#
# core logic of reading and converting the json file into dynamic class 
#
    
    def getJsonObectFromFile(self,filePath):
        #Returns the json object.

        #Parameters:
        #    filepath (str):The string which is file name with path.
    
        #Returns:
        #    JSon(Object):The object which gets from the file.   

        # Opening JSON file
        f = open(filePath)
        data = None
        try:
            # returns JSON object as a dictionary
            data = json.load(f)
        except:
            print("Invalid JSon file, please provide valid file")
        finally:
            f.close()
            return  data
        
    
    def getKeys(self, listData):
        #Returns the list.

        #Parameters:
        #    listData (dict):The dictionary which is json list.
    
        #Returns:
        #    list(Object):The list which contains the key of dictionary   
        
        if listData == None:
            return listData
        keysList = []
        for key in listData:
            keysList.append(key)
        return keysList
    
    def convertJsonObjectToClass(self,filename):
        #Returns converted json file(properties) into dynamic object
        #
        #Parameters:
        #    filename (str):The string which is filename with path.
        #
        #Returns:
        #    Dynamic class instance(Object):The object which contains the properties and its values into object as attributes    
        data = self.getJsonObectFromFile(filename)
        rc = DynamicClass()
        keysList = self.getKeys(data)
        
        #validating the keysList equal to None then not performing the logic
        if keysList == None:
            return keysList
            
        # Iterating through the json
        for i in keysList:
            if type(data[i]) == dict:
                subObj = DynamicClass()
                for j in data[i]:
                    if type(data[i][j]) == dict:
                        subSubObj = DynamicClass();
                        for k in data[i][j]:
                            setattr(subSubObj, k, data[i][j][k])
                        setattr(subObj, j, subSubObj)
                    if type(data[i][j]) != dict :
                        setattr(subObj, j, data[i][j])
                setattr(rc, i, subObj)
            if type(data[i]) == str:
                setattr(rc, i, data[i])
        return rc