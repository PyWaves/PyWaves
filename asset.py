import pywaves

class Asset(object):
    def __init__(self, assetId):
        self.assetId='' if assetId == 'WAVES' else assetId
        self.issuer = self.name = self.description = ''
        self.quantity = self.decimals = 0
        self.reissuable = False
        if self.assetId=='':
            self.quantity=100000000e8
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
               'ecimals = %d\n' \
               'reissuable = %s' % (self.status(), self.assetId, self.issuer, self.name, self.description, self.quantity, self.decimals, self.reissuable)

    __repr__ = __str__

    def status(self):
        if self.assetId!='WAVES':
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

    __repr__ = __str__

WAVES = Asset('')