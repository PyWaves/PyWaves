from .helpers import Helpers
from .. import pywaves as pw
from .. import address
import pytest

pw.setThrowOnError(True)

def test_CancelWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    leasingID = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    with pytest.raises(Exception) as error:
        myAddress.leaseCancel(leasingID)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_CancelWithFeeIsBiggerThanBalance():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='G6aEiT1ih4jwLfgJ89EvULbsziixDuqnEUTpEkvZ76hv')
    leasingID = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    with pytest.raises(Exception) as error:
        myAddress.leaseCancel(leasingID)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_SuccesfullCancelLeasing():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    leasingAddress = address.Address('3MrgK5eCdrva5iVvQh1d8yGSrHQGF93Lep7')

    leaseTransaction = myAddress.lease(leasingAddress, 1 * 10 ** 8)
    helpers.waitFor(leaseTransaction['id'])

    leaseCancelTransactionId = myAddress.leaseCancel(leaseTransaction['id'])
    blockchainTx = helpers.waitFor(leaseCancelTransactionId)

    assert blockchainTx['id'] == leaseCancelTransactionId
