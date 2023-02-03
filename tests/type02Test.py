from .helpers import Helpers
from .. import pywaves as pw
from .. import address
import base58
import pywaves.crypto as crypto
import pytest

pw.setThrowOnError(True)

def test_sendWaveswithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    with pytest.raises(Exception) as error:
        myAddress.sendWaves(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), 100*10**8)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_sendWavesButSelfBalanceIsEmpty():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= 'G6aEiT1ih4jwLfgJ89EvULbsziixDuqnEUTpEkvZ76hv')

    with pytest.raises(Exception) as error:
        myAddress.sendWaves(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), 100*10**8)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_sendWavesButWithoutAmount():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= 'G6aEiT1ih4jwLfgJ89EvULbsziixDuqnEUTpEkvZ76hv')

    with pytest.raises(Exception) as error:
        myAddress.sendWaves(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), 0)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Amount must be > 0\') tblen=3>'

def test_successfulTransfer():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= 'BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    tx = myAddress.sendWaves(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), 1*10*4, txFee=500000)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_successfulTransferWithAttachment():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= 'BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    attachment = 'this is just a test'

    tx = myAddress.sendWaves(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), 1*10*4, attachment=attachment, txFee=500000)
    print(tx)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

