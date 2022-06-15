from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_succesfullBurnAsset():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('9rAYe2FPz2LfLskidVpZcW3w7spHgQXYYyXzczNeJQyu')

    txId = myAddress.burnAsset(myToken, 1)
    blockchaintx = helpers.waitFor(txId)

    assert blockchaintx['id'] == txId

def test_pywavesOfflineBurnAsset():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('9rAYe2FPz2LfLskidVpZcW3w7spHgQXYYyXzczNeJQyu')
    pw.setOffline()
    tx = myAddress.burnAsset(myToken, 1)
    pw.setOnline()

    assert tx['api-type'] == 'POST'