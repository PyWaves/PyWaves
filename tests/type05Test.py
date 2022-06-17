from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_succesfullReissueAsset():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    myToken = asset.Asset('226sJnCCEeQXushTBPtwyWY8id44ejHdvET1b9ESSAqy')

    txId = myAddress.reissueAsset(myToken, 10, reissuable=True)
    blockchaintx = helpers.waitFor(txId)

    assert blockchaintx['id'] == txId

def test_reissueAssetPywavesOffline():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    myToken = asset.Asset('226sJnCCEeQXushTBPtwyWY8id44ejHdvET1b9ESSAqy')
    pw.setOffline()
    tx = myAddress.reissueAsset(myToken, 10)
    pw.setOnline()

    assert tx['api-type'] == 'POST'