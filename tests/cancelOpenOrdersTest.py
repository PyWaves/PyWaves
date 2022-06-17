from .. import pywaves as pw
from .. import address
from .. import asset
from .. import order
import pytest
import time

pw.setThrowOnError(True)

def test_succesfullCancelOpenOrders():
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))
    order = myAddress.sell(USDN_WAVES, 1000, 250000000000, matcherFee=1000000)
    order2 = myAddress.sell(USDN_WAVES, 1000, 350000000000, matcherFee=1000000)

    time.sleep(1)
    myAddress.cancelOpenOrders(USDN_WAVES)
    time.sleep(1)

    assert order2.status() and order.status() == 'Cancelled'
