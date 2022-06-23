import pywaves as pw
from .. import Order
from .. import address
from .. import asset
import time

pw.setThrowOnError(True)

def test_cancelOrder():
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES,asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))

    order = myAddress.sell(USDN_WAVES, 100, 1000000000, matcherFee=1000000)

    orderToTest = Order(order.orderId, USDN_WAVES, myAddress)
    orderToTest.cancel()
    time.sleep(5)

    assert orderToTest.status() == 'Cancelled'