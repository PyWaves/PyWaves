from .. import pywaves as pw
from .. import address
from .. import asset
import time


pw.setThrowOnError(True)

def test_pywavesOffline():
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))
    order = myAddress.sell(USDN_WAVES, 1000, 250000, matcherFee=1000000)
    OrderId = order.orderId

    pw.setOffline()
    tx = myAddress.cancelOrderByID(USDN_WAVES, OrderId)
    pw.setOnline()
    myAddress.cancelOrder(USDN_WAVES, order)
    assert tx['api-type'] == 'POST'

def test_succesfullCancelOrderById():
    pw.setOnline()
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))
    order = myAddress.sell(USDN_WAVES, 100,250000, matcherFee=1000000)

    time.sleep(10)
    myAddress.cancelOrderByID(USDN_WAVES, order.orderId)

    assert order.status() == 'Cancelled'