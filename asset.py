import pywaves
import logging

class Asset(object):
    def __init__(self, assetId, pywaves=pywaves):
        self.pywaves = pywaves
        self.assetId='' if assetId == pywaves.DEFAULT_CURRENCY else assetId
        self.issuer = self.name = self.description = ''
        self.quantity = self.decimals = 0
        self.reissuable = False
        self.minSponsoredAssetFee = None
        if self.assetId=='':
            self.quantity=self.pywaves.wrapper('/blockchain/rewards')['totalWavesAmount']
            self.decimals=8
        else:
            self.status()

    def __str__(self):
        return 'status = %s\n' \
               'assetId = %s\n' \
               'issuer = %s\n' \
               'name = %s\n' \
               'description = %s\n' \
               'quantity = %d\n' \
               'decimals = %d\n' \
               'reissuable = %s\n' \
               'minSponsoredAssetFee = %s' % (self.status(), self.assetId, self.issuer, self.name, self.description, self.quantity, self.decimals, self.reissuable, self.minSponsoredAssetFee)

    __repr__ = __str__

    def status(self):
        if self.assetId!=pywaves.DEFAULT_CURRENCY:
            try:
                req = self.pywaves.wrapper('/assets/details/%s' % self.assetId)
                if req['assetId'] != None:
                    self.issuer = req['issuer']
                    self.quantity = req['quantity']
                    self.decimals = req['decimals']
                    self.reissuable = req['reissuable']
                    self.name = req['name'].encode('ascii', 'ignore')
                    self.description = req['description'].encode('ascii', 'ignore')
                    self.minSponsoredAssetFee = req['minSponsoredAssetFee']
                    return 'Issued'
            except:
                pass

    def isSmart(self):
        req = self.pywaves.wrapper('/transactions/info/%s' % self.assetId)

        if ('script' in req and req['script']):
            return True
        else:
            return False

class AssetPair(object):
    def __init__(self, asset1, asset2, pywaves=pywaves):
        self.pywaves = pywaves
        self.asset1 = asset1
        self.asset2 = asset2
        self.a1 = pywaves.DEFAULT_CURRENCY if self.asset1.assetId == '' else self.asset1.assetId
        self.a2 = pywaves.DEFAULT_CURRENCY if self.asset2.assetId == '' else self.asset2.assetId

    def __str__(self):
        return 'asset1 = %s\nasset2 = %s' % (self.asset1.assetId, self.asset2.assetId)

    def refresh(self):
        self.asset1.status()
        self.asset2.status()


    def first(self):
        if len(self.asset1.assetId) < len(self.asset2.assetId):
            return self.asset1
        elif self.asset1.assetId < self.asset2.assetId:
            return self.asset1
        else:
            return self.asset2

    def second(self):
        if len(self.asset1.assetId) < len(self.asset2.assetId):
            return self.asset2
        if self.asset1.assetId < self.asset2.assetId:
            return self.asset2
        else:
            return self.asset1

    def orderbook(self):
        req = self.pywaves.wrapper('/matcher/orderbook/%s/%s' % (self.a1, self.a2), host=self.pywaves.MATCHER)
        return req

    def ticker(self):
        return self.pywaves.wrapper('/v0/pairs/%s/%s' % (self.a1, self.a2), host=self.pywaves.DATAFEED)

    def last(self):
        return str(self.ticker()['data']['lastPrice'])

    def open(self):
        return str(self.ticker()['data']['firstPrice'])

    def high(self):
        return str(self.ticker()['data']['high'])

    def low(self):
        return str(self.ticker()['data']['low'])

    def close(self):
        return self.last()

    def vwap(self):
        return str(self.ticker()['data']['weightedAveragePrice'])

    def volume(self):
        return str(self.ticker()['data']['volume'])

    def priceVolume(self):
        return str(self.ticker()['data']['quoteVolume'])

    def _getMarketData(self, method, params):
        return self.pywaves.wrapper('%s/%s/%s/%s' % (method, self.a1, self.a2, params), host=self.pywaves.DATAFEED)

    def trades(self, *args):
        if len(args)==1:
            limit = args[0]
            if limit > 0 and limit <= self.pywaves.MAX_WDF_REQUEST:
                return self._getMarketData('/api/trades/', '%d' % limit)
            else:
                msg = 'Invalid request. Limit must be >0 and <= 100'
                self.pywaves.throw_error(msg)
                return logging.error(msg)
        elif len(args)==2:
            fromTimestamp = args[0]
            toTimestamp = args[1]
            return self._getMarketData('/api/trades', '%d/%d' % (fromTimestamp, toTimestamp))

    def candles(self, *args):
        if len(args)==2:
            timeframe = args[0]
            limit = args[1]
            if timeframe not in self.pywaves.VALID_TIMEFRAMES:
                msg = 'Invalid timeframe'
                self.pywaves.throw_error(msg)
                return logging.error(msg)
            elif limit > 0 and limit <= self.pywaves.MAX_WDF_REQUEST:
                return self._getMarketData('/api/candles', '%d/%d' % (timeframe, limit))
            else:
                msg = 'Invalid request. Limit must be >0 and <= 100'
                self.pywaves.throw_error(msg)
                return logging.error(msg)
        elif len(args)==3:
            timeframe = args[0]
            fromTimestamp = args[1]
            toTimestamp = args[2]
            if timeframe not in self.pywaves.VALID_TIMEFRAMES:
                msg = 'Invalid timeframe'
                self.pywaves.throw_error(msg)
                return logging.error(msg)
            else:
                return self._getMarketData('/api/candles', '%d/%d/%d' % (timeframe, fromTimestamp, toTimestamp))

    __repr__ = __str__

