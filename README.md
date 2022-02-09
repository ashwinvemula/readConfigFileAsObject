
# Read config file

This is a python program to read data from JSon file and convert the properties into object and access them using .(dot) oprator.

## What you need to know

- use python 3.6 or later
- support of json module


## Usage

Sample code

```bash
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


```


## Test cases

Provided the unittest cases go through test_readConfig.py file

 - Invalid Json file test case
    - Test case name test_readConfigInvalidJson_1
    - Test case name test_readConfigInvalidJson_2
 - Valid Json file test case
    - test_readConfigValidJson_1
    - test_readConfigValidJson_1
 - Json property retrieve  

## To run the test cases
```bash

python test_readConfig.py

```

## Output of test run

```bash

..Invalid JSon file, please provide valid file
.Invalid JSon file, please provide valid file
...
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK


```

## Windows

To run this project, you will need to download the project and run without any changes


## Mac

To run this project on Mac OS, you will need to download the project and update the filepaths of JSON files as per Mac Os

