import unittest
from lib.ConvertJsonObject import ConvertJsonObject 

class TestReadConfig(unittest.TestCase):
    
    file_valid1 = '.\\fixtures\\config.json'
    file_valid2 = '.\\fixtures\\config.local.json'
    file_invalid1 = '.\\fixtures\\config.invalid.json'
    file_invalid2 = '.\\fixtures\\config.also_invalid.json'

    myObj = ConvertJsonObject()

    def test_readConfigValidJson_1(self):
        rc = self.myObj.convertJsonObjectToClass(self.file_valid1)
        self.assertNotEqual(rc, None)

    def test_readConfigInvalidJson_1(self):
        rc = self.myObj.convertJsonObjectToClass(self.file_invalid1)
        self.assertEqual(rc, None)

    def test_readConfigInvalidJson_2(self):
        rc = self.myObj.convertJsonObjectToClass(self.file_invalid2)
        self.assertEqual(rc, None)

    def test_readConfigEnvironment(self):
        rc = self.myObj.convertJsonObjectToClass(self.file_valid1)
        self.assertEqual(rc.environment, 'production')

    def test_readConfigHost(self):
        rc = self.myObj.convertJsonObjectToClass(self.file_valid1)
        self.assertEqual(rc.database.host, 'mysql')
        
    def test_readConfigPort(self):
        rc = self.myObj.convertJsonObjectToClass(self.file_valid1)
        self.assertEqual(rc.database.port, 3306)


if __name__ == '__main__':
    unittest.main()