from .. import pywaves as pw
from .. import address
from .. import asset


pw.setThrowOnError(True)

def test_tradableBalance():
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))

    tradableBalance = myAddress.tradableBalance(USDN_WAVES)
    dollarBalance = myAddress.balance(assetId='25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT')
    wavesBalance = myAddress.balance()

    assert tradableBalance == (wavesBalance, dollarBalance)

def test_tradableBalanceButPywavesOffline():
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))

    pw.setOffline()
    request = myAddress.tradableBalance(USDN_WAVES)
    pw.setOnline()
    print(request)
    assert request['api-type'] == 'GET'