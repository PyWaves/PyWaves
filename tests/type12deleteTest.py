from .helpers import Helpers
from .. import pywaves as pw
from .. import address
import pytest

pw.setThrowOnError(True)

def test_stringDataTransaction():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    data = [{
        'type': 'string',
        'key': 'test',
        'value': 'testval'
    }]

    myAddress.dataTransaction(data)

    tx = myAddress.deleteDataEntry(data[0]['key'])
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_integerDataTransaction():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    data = [{
        'type': 'integer',
        'key': 'testint',
        'value': 1234
    }]

    myAddress.dataTransaction(data)

    tx = myAddress.deleteDataEntry(data[0]['key'])
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_booleanDataTransaction():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    data = [{
        'type': 'boolean',
        'key': 'test',
        'value': True
    }]

    myAddress.dataTransaction(data)

    tx = myAddress.deleteDataEntry(data[0]['key'])
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_binaryDataTransaction():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    data = [{
        'type': 'binary',
        'key': 'test',
        'value': 'BzWHaQU'
    }]

    myAddress.dataTransaction(data)

    tx = myAddress.deleteDataEntry(data[0]['key'])
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']