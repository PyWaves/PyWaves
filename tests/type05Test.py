from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_succesfullReissueAsset():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('AFzTeKRwyomQ2wMtzBFriMzwJPG6HEJY3pbc8JrV6Z14')

    txId = myAddress.reissueAsset(myToken, 10, reissuable=True)
    blockchaintx = helpers.waitFor(txId)

    assert blockchaintx['id'] == txId

def test_reissueAssetPywavesOffline():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('AzLBsYko4sy5gABTcSVUyRCgv6EHhtP58qY89nqHU2uu')
    pw.setOffline()
    tx = myAddress.reissueAsset(myToken, 10)
    pw.setOnline()

    assert tx['api-type'] == 'POST'