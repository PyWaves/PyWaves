import pywaves

class Order(object):
    def __init__(self, orderId, assetPair, address = ''):
        self.orderId = orderId
        self.assetPair = assetPair
        self.address = address
        self.matcher = pywaves.MATCHER
        self.matcherPublicKey = pywaves.MATCHER_PUBLICKEY
        self.checkStatus()

    def __str__(self):
        self.checkStatus()
        return 'id = %s\n' \
               '%s\n' \
               'sender.address = %s\n' \
               'sender.publicKey = %s\n' \
               'matcher = %s\n' \
               'status = %s' % (self.orderId, self.assetPair, self.address.address, self.address.publicKey, self.matcher, self.status)

    def checkStatus(self):
        self.status = ''
        try:
            req = pywaves.wrapper('/matcher/orderbook/%s/%s/%s' % (self.assetPair.asset1.assetId, self.assetPair.asset2.assetId, self.orderId), host=self.matcher)
            if req['status'] == 'Accepted':
                self.status = 'ACCEPTED'
            elif req['status'] == 'Filled':
                self.status = 'FILLED'
            elif req['status'] == 'Cancelled':
                self.status = 'CANCELLED'
        except:
            pass
        return self.status

    def cancel(self):
        if self.address:
            self.address.cancelOrder(self.assetPair, self)

    __repr__ = __str__
