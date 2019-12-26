import requests
import pywaves as pw

class Oracle(object):

    def __init__(self, oracleAddress = None, seed = None):
        if seed != None:
            self.oracleAddress = pw.Address(seed=seed)
        else:
            self.oracleAddress = oracleAddress

    def getData(self, key = None, regex = None):
        if key == None and regex == None:
            result = self._getDataWithoutKey()
        elif key != None:
            result = self._getDataWithKey(key)
        elif regex != None:
            result = self._getDataWithRegex(regex)

        return result

    def _getDataWithRegex(self, regex):
        print(pw.NODE + '/addresses/data/' + self.oracleAddress + '?matches=' + regex)
        return requests.get(pw.NODE + '/addresses/data/' + self.oracleAddress + '?matches=' + regex).json()

    def _getDataWithoutKey(self):
        return requests.get(pw.NODE + '/addresses/data/' + self.oracleAddress).json()

    def _getDataWithKey(self, key):
        return requests.get(pw.NODE + '/addresses/data/' + self.oracleAddress + '/' + key).json()['value']

    def storeData(self, key, type, dataEntry):
        dataToStore = [{
            'type': type,
            'key': key,
            'value': dataEntry
        }]

        return self.oracleAddress.dataTransaction(dataToStore)
