from .. import pywaves as pw
from .. import WXFeeCalculator
import requests


matcher = 'https://dex.polarity.exchange'

def test_getCalculatePercentBuyingFee():
    pw.setMatcher(matcher)
    pw.setNode('http://cluster.tnnode.turtlenetwork.eu', 'L')
    priceAssetId = '5bXgvADuVoFdhtF5uKZAEiVdAo7ZCWw151L4yyf1PiES'
    amountAssetId = 'EzwaF58ssALcUCZ9FbyeD1GTSteoZAQZEDTqBAXHfq8y'
    price = 2517500
    amount = 500000000
    wxFeeCalculator = WXFeeCalculator()

    requestedFees = requests.post(
        matcher + '/matcher/orderbook/' + amountAssetId + '/' + priceAssetId + '/calculateFee',
        json={"orderType": "buy", "amount": amount, "price": price}).json()

    calculatedFee = wxFeeCalculator.calculatePercentBuyingFee(amountAssetId, priceAssetId, price, amount)

    assert calculatedFee >= requestedFees['base']['matcherFee']
