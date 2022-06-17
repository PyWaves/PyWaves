from .helpers import Helpers
from .. import pywaves as pw
from .. import address
import pytest

pw.setThrowOnError(True)

def test_MassTransferWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 200},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 200}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferWaves(transfers)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_MassTransferWithoutEnoughWaves():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= 'BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 2000000000000000000},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 2000000000000000000}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferWaves(transfers)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_succesfullMassTransfer():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= 'BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 10000},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 10000}
    ]

    tx = myAddress.massTransferWaves(transfers)
    print('tx: ' + str(tx))
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_MassTransferWithTooMuchRecipients():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100}

    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferWaves(transfers)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Too many recipients\') tblen=3>'