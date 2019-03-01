import pywaves
import logging

class Asset(object):
    def __init__(self, assetId):
        self.assetId = '' if assetId == 'WAVES' else assetId
        self._quantity = None
        self._decimals = None
        self._issuer = None
        self._name = None
        self._description = None
        self._reissuable = None
        self._script = None

    def __str__(self):
        return 'assetId = %s\n' \
               'issuer = %s\n' \
               'name = %s\n' \
               'description = %s\n' \
               'quantity = %d\n' \
               'decimals = %d\n' \
               'reissuable = %s' % (self.assetId, self.issuer, self.name, self.description, self.quantity, self.decimals, self.reissuable)

    __repr__ = __str__

    def update(self):
        if self.assetId == '':
            self._quantity=100000000e8
            self._decimals=8
            self._issuer = ''
            self._name = ''
            self._description = ''
            self._reissuable = False
            self._script = ''
            return

        req = pywaves.wrapper('/transactions/info/%s' % self.assetId)
        if req['type'] != 3:
            raise Exception('Invalid asset id')
        self._quantity = req['quantity']
        self._decimals = req['decimals']
        self._issuer = req['sender']
        self._name = req['name'].encode('ascii', 'ignore')
        self._description = req['description'].encode('ascii', 'ignore')
        self._reissuable = req['reissuable']
        self._script = req['script'] if 'script' in req else ''

    def isSmart(self):
        return True if self.script else False


def get_getter(name):
    def getter(self):
        value = getattr(self, '_' + name)
        if value is None:
            self.update()
            return getattr(self, '_' + name)
        return value
    return getter


fields = ['quantity', 'decimals', 'issuer', 'name', 'description', 'reissuable', 'script']
for field in fields:
    setattr(Asset, field, property(get_getter(field)))


class AssetPair(object):
    def __init__(self, asset1, asset2):
        self.asset1 = asset1
        self.asset2 = asset2
        self.a1 = 'WAVES' if self.asset1.assetId == '' else self.asset1.assetId
        self.a2 = 'WAVES' if self.asset2.assetId == '' else self.asset2.assetId

    def __str__(self):
        return 'asset1 = %s\nasset2 = %s' % (self.asset1.assetId, self.asset2.assetId)

    def first(self):
        if pywaves.getAssetPriority(self.asset1.assetId) < pywaves.getAssetPriority(self.asset2.assetId):
            return self.asset1
        elif pywaves.getAssetPriority(self.asset1.assetId) > pywaves.getAssetPriority(self.asset2.assetId):
            return self.asset2
        elif len(self.asset1.assetId) < len(self.asset2.assetId):
            return self.asset1
        elif self.asset1.assetId < self.asset2.assetId:
            return self.asset1
        else:
            return self.asset2

    def second(self):
        if pywaves.getAssetPriority(self.asset1.assetId) < pywaves.getAssetPriority(self.asset2.assetId):
            return self.asset2
        elif pywaves.getAssetPriority(self.asset1.assetId) > pywaves.getAssetPriority(self.asset2.assetId):
            return self.asset1
        elif len(self.asset1.assetId) < len(self.asset2.assetId):
            return self.asset2
        if self.asset1.assetId < self.asset2.assetId:
            return self.asset2
        else:
            return self.asset1

    def ordered(self):
        return AssetPair(self.first(), self.second())

    def orderbook(self):
        req = pywaves.wrapper('/matcher/orderbook/%s/%s' % (self.a1, self.a2), host=pywaves.MATCHER)
        return req

    def ticker(self):
        return pywaves.wrapper('/api/ticker/%s/%s' % (self.a1, self.a2), host=pywaves.DATAFEED)

    def last(self):
        return str(self.ticker()['24h_close'])

    def open(self):
        return str(self.ticker()['24h_open'])

    def high(self):
        return str(self.ticker()['24h_high'])

    def low(self):
        return str(self.ticker()['24h_low'])

    def close(self):
        return self.last()

    def vwap(self):
        return str(self.ticker()['24h_vwap'])

    def volume(self):
        return str(self.ticker()['24h_volume'])

    def priceVolume(self):
        return str(self.ticker()['24h_priceVolume'])

    def _getMarketData(self, method, params):
        return pywaves.wrapper('%s/%s/%s/%s' % (method, self.a1, self.a2, params), host=pywaves.DATAFEED)

    def trades(self, *args):
        if len(args)==1:
            limit = args[0]
            if limit > 0 and limit <= pywaves.MAX_WDF_REQUEST:
                return self._getMarketData('/api/trades/', '%d' % limit)
            else:
                msg = 'Invalid request. Limit must be >0 and <= 100'
                pywaves.throw_error(msg)
                return logging.error(msg)
        elif len(args)==2:
            fromTimestamp = args[0]
            toTimestamp = args[1]
            return self._getMarketData('/api/trades', '%d/%d' % (fromTimestamp, toTimestamp))

    def candles(self, *args):
        if len(args)==2:
            timeframe = args[0]
            limit = args[1]
            if timeframe not in pywaves.VALID_TIMEFRAMES:
                msg = 'Invalid timeframe'
                pywaves.throw_error(msg)
                return logging.error(msg)
            elif limit > 0 and limit <= pywaves.MAX_WDF_REQUEST:
                return self._getMarketData('/api/candles', '%d/%d' % (timeframe, limit))
            else:
                msg = 'Invalid request. Limit must be >0 and <= 100'
                pywaves.throw_error(msg)
                return logging.error(msg)
        elif len(args)==3:
            timeframe = args[0]
            fromTimestamp = args[1]
            toTimestamp = args[2]
            if timeframe not in pywaves.VALID_TIMEFRAMES:
                msg = 'Invalid timeframe'
                pywaves.throw_error(msg)
                return logging.error(msg)
            else:
                return self._getMarketData('/api/candles', '%d/%d/%d' % (timeframe, fromTimestamp, toTimestamp))

    __repr__ = __str__

