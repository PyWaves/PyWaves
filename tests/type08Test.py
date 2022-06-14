from .helpers import Helpers
from .. import pywaves as pw
from .. import address
import pytest

pw.setThrowOnError(True)

def test_leasingWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    leasinAdress = address.Address('3MrgK5eCdrva5iVvQh1d8yGSrHQGF93Lep7')

    with pytest.raises(Exception) as error:
        myAddress.lease(leasinAdress, 1*10**8)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_leasingWithAmountSmallerEqualsZero():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= '6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    leasinAdress = address.Address('3MrgK5eCdrva5iVvQh1d8yGSrHQGF93Lep7')

    with pytest.raises(Exception) as error:
        myAddress.lease(leasinAdress, -100000)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Amount must be > 0\') tblen=3>'

def test_BalanceSmallerThanAmount():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    leasinAdress = address.Address('3MrgK5eCdrva5iVvQh1d8yGSrHQGF93Lep7')

    with pytest.raises(Exception) as error:
        myAddress.lease(leasinAdress, 10000000000000000000000)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_succesfullLeasing():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    leasinAdress = address.Address('3MrgK5eCdrva5iVvQh1d8yGSrHQGF93Lep7')

    tx = myAddress.lease(leasinAdress, 1*10**8)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

    myAddress.leaseCancel(tx['id'])