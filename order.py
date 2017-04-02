import pywaves

class Order(object):
    def __init__(self, orderId, assetPair, address = ''):
        self.orderId = orderId
        self.assetPair = assetPair
        self.address = address
        self.matcher = pywaves.MATCHER
        self.matcherPublicKey = pywaves.MATCHER_PUBLICKEY
        self.status()

    def __str__(self):
        return 'status = %s\n' \
               'id = %s\n' \
               '%s\n' \
               'sender.address = %s\n' \
               'sender.publicKey = %s\n' \
               'matcher = %s' % (self.status(), self.orderId, self.assetPair, self.address.address, self.address.publicKey, self.matcherPublicKey)

    def status(self):
        try:
            req = pywaves.wrapper('/matcher/orderbook/%s/%s/%s' % ('WAVES' if self.assetPair.asset1.assetId=='' else self.assetPair.asset1.assetId, 'WAVES' if self.assetPair.asset2.assetId=='' else self.assetPair.asset2.assetId, self.orderId), host=self.matcher)
            return req['status']
        except:
            pass

    def cancel(self):
        if self.address:
            self.address.cancelOrder(self.assetPair, self)

    __repr__ = __str__
