from .. import pywaves as pw
from .. import address
from .. import asset
from .. import order
import pytest
import time

pw.setThrowOnError(True)


def test_pywavesOfflineCancelOrder():
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES,asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT') )
    order = myAddress.sell(USDN_WAVES, 1000, 250000000000, matcherFee=1000000)

    pw.setOffline()
    tx = myAddress.cancelOrder(USDN_WAVES, order)
    pw.setOnline()
    myAddress.cancelOrder(USDN_WAVES, order)
    assert tx['api-type'] == 'POST'

def test_orderFilled():
    pw.setOnline()
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))
    order = myAddress.sell(USDN_WAVES, 10000, 1, matcherFee= 1000000)

    with pytest.raises(Exception) as error:
        myAddress.cancelOrder(USDN_WAVES, order)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Order already filled\') tblen=3>'

def test_orderWithoutStatus():
    pw.setOnline()
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))
    orderId = '9JtTmjBqYvrkLuEPmHAJCfuc3cM2FzRNdxH7YKrpz1'
    notExistingOrder = order.Order(orderId, USDN_WAVES)

    with pytest.raises(Exception) as error:
        myAddress.cancelOrder(USDN_WAVES, notExistingOrder)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Order not found\') tblen=3>'


def test_succesfullCancelOrder():
    pw.setOnline()
    pw.setMatcher('https://testnet.waves.exchange/api/v1/forward/matcher')
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    USDN_WAVES = asset.AssetPair(pw.WAVES, asset.Asset('25FEqEjRkqK6yCkiT7Lz6SAYz7gUFCtxfCChnrVFD5AT'))
    order = myAddress.sell(USDN_WAVES, 1000, 250000000000, matcherFee=1000000)

    time.sleep(10)
    tx = myAddress.cancelOrder(USDN_WAVES, order)
    time.sleep(10)

    assert order.status() == 'Cancelled'