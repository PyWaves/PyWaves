import pywaves

class Asset(object):
    def __init__(self, assetId):
        self.assetId = assetId
        self.issuer = self.name = self.description = ''
        self.quantity = self.decimals = 0
        self.reissuable = False
        self.status()

    def __str__(self):
        return 'status = %s\n' \
               'assetId = %s\n' \
               'issuer = %s\n' \
               'name = %s\n' \
               'description = %s\n' \
               'quantity = %d\n' \
               'ecimals = %d\n' \
               'reissuable = %s' % (self.status(), self.assetId, self.issuer, self.name, self.description, self.quantity, self.decimals, self.reissuable)

    __repr__ = __str__

    def status(self):
        try:
            req = pywaves.wrapper('/transactions/info/%s' % self.assetId)
            if req['type'] == 3:
                self.issuer = req['sender']
                self.quantity = req['quantity']
                self.decimals = req['decimals']
                self.reissuable = req['reissuable']
                self.name = req['name']
                self.description = req['description']
                return 'Issued'
        except:
            pass

class AssetPair(object):
    def __init__(self, asset1, asset2):
        self.asset1 = asset1
        self.asset2 = asset2

    def __str__(self):
        return 'asset1 = %s\nasset2 = %s' % (self.asset1.assetId, self.asset2.assetId)

    def refresh(self):
        self.asset1.status()
        self.asset2.status()

    __repr__ = __str__
