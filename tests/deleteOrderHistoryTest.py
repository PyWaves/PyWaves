from .. import pywaves as pw
from .. import address
from .. import asset

pw.setThrowOnError(True)

def _deleteOrderHistory():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))

    myAddress.deleteOrderHistory(USDN_WAVES)

    tx = myAddress.getOrderHistory(USDN_WAVES)
    print(tx)

    assert len(tx) == 0
