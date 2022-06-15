
from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)
pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')

def test_buyPywavesOffline():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='G6aEiT1ih4jwLfgJ89EvULbsziixDuqnEUTpEkvZ76hv')
    USDN_WAVES = asset.AssetPair(asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'), asset.Asset('WAVES'))

    pw.setOffline()
    tx = myAddress.buy(USDN_WAVES, 10, 4600)
    pw.setOnline()

    assert tx['api-type'] == 'POST'

def test_succesfullBuyOrder():
    helpers = Helpers()
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    USDN_WAVES = asset.AssetPair(pw.WAVES,asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))

    order = myAddress.buy(USDN_WAVES, 100, 1, matcherFee=165979, matcherFeeAssetId = '25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT')
    orderStatus = order.status()

    myAddress.cancelOrder(USDN_WAVES, order)
    assert orderStatus == 'Accepted'