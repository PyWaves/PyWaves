from .helpers import Helpers
from .. import pywaves as pw
from .. import address
import pytest

pw.setThrowOnError(True)

def test_cancelWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    leasingID = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    with pytest.raises(Exception) as error:
        myAddress.leaseCancel(leasingID)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_cancelWithFeeIsBiggerThanBalance():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='G6aEiT1ih4jwLfgJ89EvULbsziixDuqnEUTpEkvZ76hv')
    leasingID = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    with pytest.raises(Exception) as error:
        myAddress.leaseCancel(leasingID)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_succesfullCancelLeasing():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    leasingAddress = address.Address('3MrgK5eCdrva5iVvQh1d8yGSrHQGF93Lep7')

    leaseTransaction = myAddress.lease(leasingAddress, 1 * 10 ** 8)
    helpers.waitFor(leaseTransaction['id'])
    print(leaseTransaction['id'])

    leaseCancelTransactionId = myAddress.leaseCancel(leaseTransaction['id'])
    print(leaseCancelTransactionId)
    blockchainTx = helpers.waitFor(leaseCancelTransactionId)

    assert blockchainTx['id'] == leaseCancelTransactionId

def test_pywavesOffline():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    pw.setOffline()
    leaseCancelTransactionId = myAddress.leaseCancel('3sEGi6tL8Ptg4L9wJv8FZRYu1hJxFJrWZGC4tWVrcycS')
    pw.setOnline()

    assert leaseCancelTransactionId['api-type'] == 'POST'
