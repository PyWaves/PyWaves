import pywaves

class Asset(object):
    def __init__(self, assetId):
        self.status = 'PENDING'
        self.assetId = assetId
        self.issuer = self.name = self.description = ''
        self.quantity = self.decimals = 0
        self.reissuable = False
        self.issued()

    def __str__(self):
        self.issued()
        return 'status = %s\nassetId = %s\nissuer = %s\nname = %s\ndescription = %s\nquantity = %d\ndecimals = %d\nreissuable = %s' % (self.status, self.assetId, self.issuer, self.name, self.description, self.quantity, self.decimals, self.reissuable)

    __repr__ = __str__

    def issued(self):
        try:
            req = pywaves.wrapper('/transactions/info/%s' % self.assetId)
            if req['type'] == 3:
                self.issuer = req['sender']
                self.quantity = req['quantity']
                self.decimals = req['decimals']
                self.reissuable = req['reissuable']
                self.name = req['name']
                self.description = req['description']
                self.status = 'ISSUED'
                return True
        except:
            pass
        return False

class AssetPair(object):
    def __init__(self, asset1, asset2):
        self.asset1 = asset1
        self.asset2 = asset2

    def __str__(self):
        return 'asset1 = %s\nasset2 = %s' % (self.asset1.assetId, self.asset2.assetId)

    __repr__ = __str__
