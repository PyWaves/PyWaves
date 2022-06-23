import pywaves
from .. import pywaves as pw
import requests
import time

class Helpers:

    def waitFor(self, id):
        pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
        response = requests.get(pw.NODE + '/transactions/info/' + id).json()

        if 'error' in response:
            time.sleep(1)
            return self.waitFor(id)
        else:
            return response
