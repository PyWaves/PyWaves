from .. import pywaves as pw
from .. import WXFeeCalculator
import requests

pw.setMatcher('https://matcher.waves.exchange')

def test_getCalculatePercentDiscountedBuyingFee():
    pw.setMatcher('https://matcher.waves.exchange')
    pw.setNode('https://nodes.wavesnodes.com')
    matcher = 'https://matcher.waves.exchange'
    priceAssetId = 'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p'
    amountAssetId = 'WAVES'
    price = 10 * 10 ** 6
    amount = 10 * 10 ** 8
    wxFeeCalculator = WXFeeCalculator()

    requestedFees = requests.post(
        matcher + '/matcher/orderbook/' + amountAssetId + '/' + priceAssetId + '/calculateFee',
        json={"orderType": "buy", "amount": amount, "price": price}).json()

    calculatedFee = wxFeeCalculator.calculatePercentDiscountedBuyingFee(priceAssetId, price, amount)

    assert calculatedFee >= requestedFees['discount']['matcherFee']

def test_getCalculatePercentDiscountedSellingFee():
    pw.setMatcher('https://matcher.waves.exchange')
    matcher = 'https://matcher.waves.exchange'
    priceAssetId = 'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p'
    amountAssetId = 'WAVES'
    price = 10 * 10 ** 6
    amount = 10 * 10 ** 8
    wxFeeCalculator = WXFeeCalculator()

    requestedFees = requests.post(
        matcher + '/matcher/orderbook/' + amountAssetId + '/' + priceAssetId + '/calculateFee',
        json={"orderType": "sell", "amount": amount, "price": price}).json()

    calculatedFee = wxFeeCalculator.calculatePercentDiscountedSellingFee(priceAssetId, amountAssetId, amount)

    assert calculatedFee >= requestedFees['discount']['matcherFee']

def test_getCalculatePercentBuyingFee():
    pw.setMatcher('https://matcher.waves.exchange')
    pw.setNode('https://nodes.wavesnodes.com')
    matcher = 'https://matcher.waves.exchange'
    priceAssetId = 'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p'
    amountAssetId = 'WAVES'
    price = 10 * 10 ** 6
    amount = 10 * 10 ** 8
    wxFeeCalculator = WXFeeCalculator()

    requestedFees = requests.post(
        matcher + '/matcher/orderbook/' + amountAssetId + '/' + priceAssetId + '/calculateFee',
        json={"orderType": "buy", "amount": amount, "price": price}).json()

    calculatedFee = wxFeeCalculator.calculatePercentBuyingFee(priceAssetId, price, amount)

    assert calculatedFee >= requestedFees['base']['matcherFee']


def test_getCalculatePercentSellingFee():
    pw.setMatcher('https://matcher.waves.exchange')
    matcher = 'https://matcher.waves.exchange'
    priceAssetId = 'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p'
    amountAssetId = 'WAVES'
    price = 10 * 10 ** 6
    amount = 10 * 10 ** 8
    wxFeeCalculator = WXFeeCalculator()

    requestedFees = requests.post(
        matcher + '/matcher/orderbook/' + amountAssetId + '/' + priceAssetId + '/calculateFee',
        json={"orderType": "sell", "amount": amount, "price": price}).json()

    calculatedFee = wxFeeCalculator.calculatePercentSellingFee(priceAssetId, amountAssetId, amount)

    assert calculatedFee >= requestedFees['base']['matcherFee']

def test_discountedFee():
    pw.setMatcher('https://matcher.waves.exchange')
    matcher = 'https://matcher.waves.exchange'
    priceAssetId = 'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p'
    amountAssetId = 'bPWkA3MNyEr1TuDchWgdpqJZhGhfPXj7dJdr3qiW2kD'
    price = 10 * 10 ** 6
    amount = 10 * 10 ** 8
    wxFeeCalculator = WXFeeCalculator()

    requestedFees = requests.post(
        matcher + '/matcher/orderbook/' + amountAssetId + '/' + priceAssetId + '/calculateFee',
        json={"orderType": "sell", "amount": amount, "price": price}).json()

    calculatedFee = wxFeeCalculator.calculateDynamicDiscountFee()

    assert calculatedFee >= requestedFees['discount']['matcherFee']

def test_dynamicFee():
    pw.setMatcher('https://matcher.waves.exchange')
    matcher = 'https://matcher.waves.exchange'
    priceAssetId = 'DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p'
    amountAssetId = 'bPWkA3MNyEr1TuDchWgdpqJZhGhfPXj7dJdr3qiW2kD'
    price = 10 * 10 ** 6
    amount = 10 * 10 ** 8
    wxFeeCalculator = WXFeeCalculator()

    requestedFees = requests.post(
        matcher + '/matcher/orderbook/' + amountAssetId + '/' + priceAssetId + '/calculateFee',
        json={"orderType": "sell", "amount": amount, "price": price}).json()

    calculatedFee = wxFeeCalculator.calculateDynamicFee()

    assert calculatedFee >= requestedFees['base']['matcherFee']
