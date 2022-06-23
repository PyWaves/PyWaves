import pywaves as pw
from .. import Oracle
from .helpers import Helpers


pw.setThrowOnError(True)

def test_getDataWithKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    oracle = Oracle(oracleAddress= '3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm', seed='muffin action girl between across budget business bid hero jazz hurdle opinion kiwi daring inmate')
    data = oracle.getData(key = 'Hello_0')


    assert data != None

def test_getDataWithoutKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    oracle = Oracle(oracleAddress= '3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    data = oracle.getData(key = None)

    assert len(data) != 0

def test_getDataWithRegex():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    oracle = Oracle(oracleAddress='3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    data = oracle.getData(regex='^Hello_.*$')

    assert data != None

def test_storeData():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    oracle = Oracle(oracleAddress= '3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm', seed='muffin action girl between across budget business bid hero jazz hurdle opinion kiwi daring inmate')

    tx = oracle.storeData(type='string', key= 'test33', dataEntry='Hello')
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']
