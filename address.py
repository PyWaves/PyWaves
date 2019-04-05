import math
import pywaves
import axolotl_curve25519 as curve
import os
import pywaves.crypto as crypto
import time
import struct
import json
import base58
import base64
import logging
import requests

class Address(object):
    def __init__(self, address='', publicKey='', privateKey='', seed='', alias='', nonce=0):
        if nonce < 0 or nonce > 4294967295:
            raise ValueError('Nonce must be between 0 and 4294967295')

        if alias and not pywaves.OFFLINE:
            address = pywaves.wrapper('/alias/by-alias/%s' % alias).get("address", "")

        if not alias and not address and not publicKey and not privateKey and not seed:
            from seed import generate_seed
            seed = generate_seed()

        self.seed = seed
        self.nonce = nonce

        self.address, self.publicKey, self.privateKey = crypto.generate_key(address=address, public_key=publicKey, private_key=privateKey, seed=seed, nonce=nonce)

        if self.address and not pywaves.validateAddress(self.address):
            raise ValueError("Invalid address")

        if not pywaves.OFFLINE:
            self.aliases = self.aliases()

    def __str__(self):
        if self.address:
            ab = []
            try:
                for a in self.balances():
                    if a['balance'] > 0:
                        ab.append("  %s (%s) = %d" % (a['assetId'], a['issueTransaction']['name'].encode('ascii', 'ignore'), a['balance']))
            except:
                pass
            return 'address = %s\npublicKey = %s\nprivateKey = %s\nseed = %s\nnonce = %d\nbalances:\n  Waves = %d%s' % (self.address, self.publicKey, self.privateKey, self.seed, self.nonce, self.balance(), '\n'+'\n'.join(ab) if ab else '')

    __repr__ = __str__

    def balances(self):
        return pywaves.wrapper('/assets/balance/%s' % self.address)['balances']

    def balance(self, assetId='', confirmations=0):
        try:
            if assetId:
                return pywaves.wrapper('/assets/balance/%s/%s' % (self.address, assetId))['balance']
            else:
                return pywaves.wrapper('/addresses/balance/%s%s' % (self.address, '' if confirmations==0 else '/%d' % confirmations))['balance']
        except:
            return 0

    def assets(self):
        req = pywaves.wrapper('/assets/balance/%s' % self.address)['balances']
        return [r['assetId'] for r in req]

    def aliases(self):
        a = pywaves.wrapper('/alias/by-address/%s' % self.address)
        if type(a)==list:
            for i in range(len(a)):
                a[i] = a[i][8:]
        return a

    def _generate(self, publicKey='', privateKey='', seed='', nonce=0):
        self.seed = seed
        self.nonce = nonce
        if not publicKey and not privateKey and not seed:
            from seed import generate_seed
            self.seed = generate_seed()
        if publicKey:
            pubKey = base58.b58decode(bytes(publicKey))
            privKey = ""
        else:
            seedHash = crypto.hashChain(struct.pack(">L", nonce) + crypto.str2bytes(self.seed))
            accountSeedHash = crypto.sha256(seedHash)
            if not privateKey:
                privKey = curve.generatePrivateKey(accountSeedHash)
            else:
                privKey = base58.b58decode(bytes(privateKey))
            pubKey = curve.generatePublicKey(privKey)
        unhashedAddress = chr(1) + bytes(pywaves.CHAIN_ID) + crypto.hashChain(pubKey)[0:20]
        addressHash = crypto.hashChain(crypto.str2bytes(unhashedAddress))[0:4]
        self.address = base58.b58encode(crypto.str2bytes(unhashedAddress + addressHash))
        self.publicKey = base58.b58encode(pubKey)
        if privKey != "":
            self.privateKey = base58.b58encode(privKey)

    def issueAsset(self, name, description, quantity, decimals=0, reissuable=False, txFee=pywaves.DEFAULT_ASSET_FEE):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif len(name) < 4 or len(name) > 16:
            msg = 'Asset name must be between 4 and 16 characters long'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            timestamp = int(time.time() * 1000)
            sData = b'\3' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    struct.pack(">H", len(name)) + \
                    crypto.str2bytes(name) + \
                    struct.pack(">H", len(description)) + \
                    crypto.str2bytes(description) + \
                    struct.pack(">Q", quantity) + \
                    struct.pack(">B", decimals) + \
                    (b'\1' if reissuable else b'\0') + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp)
            signature=crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "name": name,
                "quantity": quantity,
                "timestamp": timestamp,
                "description": description,
                "decimals": decimals,
                "reissuable": reissuable,
                "fee": txFee,
                "signature": signature
            })
            req = pywaves.wrapper('/assets/broadcast/issue', data)
            if pywaves.OFFLINE:
                return req
            else:
                return pywaves.Asset(req['assetId'])

    def reissueAsset(self, Asset, quantity, reissuable=False, txFee=pywaves.DEFAULT_TX_FEE):
        timestamp = int(time.time() * 1000)
        sData = b'\5' + \
                base58.b58decode(bytes(self.publicKey)) + \
                base58.b58decode(bytes(Asset.assetId)) + \
                struct.pack(">Q", quantity) + \
                (b'\1' if reissuable else b'\0') + \
                struct.pack(">Q",txFee) + \
                struct.pack(">Q", timestamp)
        signature = crypto.sign(self.privateKey, sData)
        data = json.dumps({
            "senderPublicKey": self.publicKey,
            "assetId": Asset.assetId,
            "quantity": quantity,
            "timestamp": timestamp,
            "reissuable": reissuable,
            "fee": txFee,
            "signature": signature
        })
        req = pywaves.wrapper('/assets/broadcast/reissue', data)
        if pywaves.OFFLINE:
            return req
        else:
            return req.get('id', 'ERROR')

    def burnAsset(self, Asset, quantity, txFee=pywaves.DEFAULT_TX_FEE):
        timestamp = int(time.time() * 1000)

        sData = '\6' + \
                crypto.bytes2str(base58.b58decode(bytes(self.publicKey))) + \
                crypto.bytes2str(base58.b58decode(bytes(Asset.assetId))) + \
                crypto.bytes2str(struct.pack(">Q", quantity)) + \
                crypto.bytes2str(struct.pack(">Q", txFee)) + \
                crypto.bytes2str(struct.pack(">Q", timestamp))
        signature = crypto.sign(self.privateKey, crypto.str2bytes(sData))
        data = json.dumps({
            "senderPublicKey": self.publicKey,
            "assetId": Asset.assetId,
            "quantity": quantity,
            "timestamp": timestamp,
            "fee": txFee,
            "signature": signature
        })
        req = pywaves.wrapper('/assets/broadcast/burn', data)
        if pywaves.OFFLINE:
            return req
        else:
            return req.get('id', 'ERROR')

    def sendWaves(self, recipient, amount, attachment='', txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)

        elif amount <= 0:
            msg = 'Amount must be > 0'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < amount + txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)

        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\4' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    b'\0\0' + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", amount) + \
                    struct.pack(">Q", txFee) + \
                    base58.b58decode(bytes(recipient.address)) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "recipient": recipient.address,
                "amount": amount,
                "fee": txFee,
                "timestamp": timestamp,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature
            })

            return pywaves.wrapper('/assets/broadcast/transfer', data)

    def massTransferWaves(self, transfers, attachment='', timestamp=0):
        txFee = 100000 + (math.ceil((len(transfers) + 1) / 2 - 0.5)) * 100000
        totalAmount = 0

        for i in range(0, len(transfers)):
            totalAmount += transfers[i]['amount']

        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif len(transfers) > 100:
            msg = 'Too many recipients'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < totalAmount + txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            transfersData = b''
            for i in range(0, len(transfers)):
                transfersData += base58.b58decode(bytes(transfers[i]['recipient']) + struct.pack(">Q", transfers[i]['amount']))
            sData = b'\x0b' + \
                    b'\1' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    b'\0' + \
                    struct.pack(">H", len(transfers)) + \
                    transfersData + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)

            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 11,
                "version": 1,
                "assetId": "",
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "transfers": transfers,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def sendAsset(self, recipient, asset, amount, attachment='', feeAsset='', txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Asset not issued'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and asset and not asset.status():
            msg = 'Asset not issued'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif amount <= 0:
            msg = 'Amount must be > 0'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and asset and self.balance(asset.assetId) < amount:
            msg = 'Insufficient asset balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and not asset and self.balance() < amount:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and not feeAsset and self.balance() < txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and feeAsset and self.balance(feeAsset.assetId) < txFee:
            msg = 'Insufficient asset balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if feeAsset:
                feeInfos = pywaves.wrapper('/assets/details/' + feeAsset.assetId)
                if feeInfos['minSponsoredAssetFee']:
                    txFee = feeInfos['minSponsoredAssetFee']
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\4' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    (b'\1' + base58.b58decode(bytes(asset.assetId)) if asset else b'\0') + \
                    (b'\1' + base58.b58decode(bytes(feeAsset.assetId)) if feeAsset else b'\0') + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", amount) + \
                    struct.pack(">Q", txFee) + \
                    base58.b58decode(bytes(recipient.address)) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "assetId": (asset.assetId if asset else ""),
                "feeAssetId": (feeAsset.assetId if feeAsset else ""),
                "senderPublicKey": self.publicKey,
                "recipient": recipient.address,
                "amount": amount,
                "fee": txFee,
                "timestamp": timestamp,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature
            })

            return pywaves.wrapper('/assets/broadcast/transfer', data)

    def massTransferAssets(self, transfers, asset, attachment='', timestamp=0):
        txFee = 100000 + (math.ceil((len(transfers) + 1) / 2 - 0.5)) * 100000

        if (asset.scripted):
            txFee += 400000

        totalAmount = 0

        if not self.privateKey:
            logging.error('Private key required')
        elif len(transfers) > 100:
            logging.error('Too many recipients')
        elif not pywaves.OFFLINE and self.balance() < txFee:
            logging.error('Insufficient Waves balance')
        elif not pywaves.OFFLINE and self.balance(assetId=asset.assetId) < totalAmount:
            logging.error('Insufficient %s balance' % asset.name)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            transfersData = b''
            for i in range(0, len(transfers)):
                transfersData += base58.b58decode(bytes(transfers[i]['recipient']) + struct.pack(">Q", transfers[i]['amount']))
            sData = b'\x0b' + \
                    b'\1' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    b'\1' + \
                    base58.b58decode(bytes(asset.assetId)) + \
                    struct.pack(">H", len(transfers)) + \
                    transfersData + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)

            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 11,
                "version": 1,
                "assetId": asset.assetId,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "transfers": transfers,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def dataTransaction(self, data, timestamp=0):
        if not self.privateKey:
            logging.error('Private key required')
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            dataObject = {
                "type": 12,
                "version": 1,
                "senderPublicKey": self.publicKey,
                "data": data,
                "fee": 0,
                "timestamp": timestamp,
                "proofs": ['']
            }
            dataBinary = b''
            for i in range(0, len(data)):
                d = data[i]
                keyBytes = crypto.str2bytes(d['key'])
                dataBinary += struct.pack(">H", len(keyBytes))
                dataBinary += keyBytes
                if d['type'] == 'binary':
                    dataBinary += b'\2'
                    valueAsBytes = d['value']
                    dataBinary += struct.pack(">H", len(valueAsBytes))
                    dataBinary += crypto.str2bytes(valueAsBytes)
                elif d['type'] == 'boolean':
                    if d['value']:
                        dataBinary += b'\1\1'
                    else:
                        dataBinary += b'\1\0'
                elif d['type'] == 'integer':
                    dataBinary += b'\0'
                    dataBinary += struct.pack(">Q", d['value'])
                elif d['type'] == 'string':
                    dataBinary += b'\3'
                    dataBinary += struct.pack(">H", len(d['value']))
                    dataBinary += crypto.str2bytes(d['value'])
            # check: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
            txFee = (int(( (len(crypto.str2bytes(json.dumps(data))) + 2 + 64 )) / 1000.0) + 1 ) * 100000
            dataObject['fee'] = txFee
            sData = b'\x0c' + \
                    b'\1' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    struct.pack(">H", len(data)) + \
                    dataBinary + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", txFee)

            dataObject['proofs'] = [ crypto.sign(self.privateKey, sData) ]

            for entry in dataObject['data']:
                if entry['type'] == 'binary':
                    base64Encoded =  base64.b64encode(crypto.str2bytes(entry['value']))
                    entry['value'] = 'base64:' + crypto.bytes2str(base64Encoded)
            dataObjectJSON = json.dumps(dataObject)
            return pywaves.wrapper('/transactions/broadcast', dataObjectJSON)

    def exchange(self, spent_asset, receive_asset, spent_amount, receive_amount, maxLifetime=30*86400, matcherFee=pywaves.DEFAULT_MATCHER_FEE, timestamp=0):
        from asset import AssetPair
        pair = AssetPair(receive_asset, spent_asset).ordered()
        if pair.asset1 is receive_asset and pair.asset2 is spent_asset:
            amount = receive_amount
            price = spent_amount/receive_amount
            return self.buy(pair, amount, price, maxLifetime, matcherFee, timestamp)
        elif pair.asset1 is spent_asset and pair.asset2 is receive_asset:
            amount = spent_amount
            price = receive_amount/spent_amount
            return self.sell(pair, amount, price, maxLifetime, matcherFee, timestamp)
        else:
            raise Exception('internal error, it\'s should not happened')

    def _postOrder(self, amountAsset, priceAsset, orderType, amount, price, maxLifetime=30*86400, matcherFee=pywaves.DEFAULT_MATCHER_FEE, timestamp=0):

        from decimal import Decimal
        if not isinstance(amount, Decimal) or not isinstance(price, Decimal):
            raise Exception('Decimal type expected')
        amount = int((amount * Decimal((0, (1,), amountAsset.decimals))).to_integral_exact())
        price = int((price * Decimal((0, (1,), priceAsset.decimals))).to_integral_exact())

        if timestamp == 0:
            timestamp = int(time.time() * 1000)
        expiration = timestamp + maxLifetime * 1000
        asset1 = b'\0' if amountAsset.assetId=='' else b'\1' + base58.b58decode(bytes(amountAsset.assetId))
        asset2 = b'\0' if priceAsset.assetId=='' else b'\1' + base58.b58decode(bytes(priceAsset.assetId))
        sData = base58.b58decode(bytes(self.publicKey)) + \
                base58.b58decode(bytes(pywaves.MATCHER_PUBLICKEY)) + \
                asset1 + \
                asset2 + \
                orderType + \
                struct.pack(">Q", price) + \
                struct.pack(">Q", amount) + \
                struct.pack(">Q", timestamp) + \
                struct.pack(">Q", expiration) + \
                struct.pack(">Q", matcherFee)
        signature = crypto.sign(self.privateKey, sData)
        otype = "buy" if orderType==b'\0' else "sell"
        data = json.dumps({
            "senderPublicKey": self.publicKey,
            "matcherPublicKey": pywaves.MATCHER_PUBLICKEY,
            "assetPair": {
                "amountAsset": amountAsset.assetId,
                "priceAsset": priceAsset.assetId,
                },
            "orderType": otype,
            "price": price,
            "amount": amount,
            "timestamp": timestamp,
            "expiration": expiration,
            "matcherFee": matcherFee,
            "signature": signature
        })
        req = pywaves.wrapper('/matcher/orderbook', data, host=pywaves.MATCHER)
        """
        {u'status': u'OrderAccepted', u'message': {u'assetPair': {u'priceAsset': u'Ft8X1v1LTa1ABafufpaCWyVj8KkaxUWE6xBhW6sNFJck', u'amountAsset': None}, u'orderType': u'buy', u'price': 268, u'signature': u'4LzSfA4CDLbznAsykB8fHXtvLP6ZvaUYkSowrn6KXgouatSskHRQ1chiPdq6Hyo7yXi9cdfYdTZo6NFVk8APBXuz', u'matcherFee': 300000, u'senderPublicKey': u'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', u'amount': 387444879, u'version': 1, u'expiration': 1553609813760, u'timestamp': 1551017813760, u'proofs': [u'4LzSfA4CDLbznAsykB8fHXtvLP6ZvaUYkSowrn6KXgouatSskHRQ1chiPdq6Hyo7yXi9cdfYdTZo6NFVk8APBXuz'], u'id': u'CGchfxnGKsySb36SPziRXo7AoijPUPvYReuXN9KczRwT', u'matcherPublicKey': u'7kPFrHDiGw1rCm7LPszuECwWYL3dMf6iMifLRDJQZMzy', u'sender': u'3XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}}
        """
        id = -1
        if 'status' in req:
            if req['status'] == 'OrderRejected':
                msg = 'Order Rejected - %s' % req['message']
                logging.error(msg)
                pywaves.throw_error(msg)
            elif req['status'] == 'OrderAccepted':
                id = str(req['message']['id'])
                logging.info('Order Accepted - ID: %s' % id)
        elif not pywaves.OFFLINE:
            logging.error(req)
            pywaves.throw_error(req)
        else:
            return req
        return id

    def cancelOrder(self, assetPair, order):
        if not pywaves.OFFLINE:
            if order.status() == 'Filled':
                msg = "Order already filled"
                logging.error(msg)
                pywaves.throw_error(msg)

            elif not order.status():
                msg = "Order not found"
                logging.error(msg)
                pywaves.throw_error(msg)
        sData = base58.b58decode(bytes(self.publicKey)) + \
                base58.b58decode(bytes(order.orderId))
        signature = crypto.sign(self.privateKey, sData)
        data = json.dumps({
            "sender": self.publicKey,
            "orderId": order.orderId,
            "signature": signature
        })
        req = pywaves.wrapper('/matcher/orderbook/%s/%s/cancel' % ('WAVES' if assetPair.asset1.assetId=='' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId=='' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)
        if pywaves.OFFLINE:
            return req
        else:
            id = -1
            if req['status'] == 'OrderCanceled':
                id = req['orderId']
                logging.info('Order Cancelled - ID: %s' % id)
            return id

    def cancelOrderByID(self, assetPair, orderId):
        sData = base58.b58decode(bytes(self.publicKey)) + \
                base58.b58decode(bytes(orderId))
        signature = crypto.sign(self.privateKey, sData)
        data = json.dumps({
            "sender": self.publicKey,
            "orderId": orderId,
            "signature": signature
        })
        req = pywaves.wrapper('/matcher/orderbook/%s/%s/cancel' % ('WAVES' if assetPair.asset1.assetId=='' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId=='' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)
        if 'message' in req:
            raise Exception(req['message'])
        if req['status'] == 'OrderCanceled':
            logging.info('Order Cancelled - ID: %s' % orderId)
            return
        raise Exception('Order was not canceled')

    def deleteOrderByID(self, assetPair, orderId):
        sData = base58.b58decode(bytes(self.publicKey)) + \
                base58.b58decode(bytes(orderId))
        signature = crypto.sign(self.privateKey, sData)
        data = json.dumps({
            "sender": self.publicKey,
            "orderId": orderId,
            "signature": signature
        })
        pywaves.wrapper('/matcher/orderbook/%s/%s/delete' % ('WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)

    def buy(self, assetPair, amount, price, maxLifetime=30 * 86400, matcherFee=pywaves.DEFAULT_MATCHER_FEE, timestamp=0):
        id = self._postOrder(assetPair.asset1, assetPair.asset2, b'\0', amount, price, maxLifetime, matcherFee, timestamp)
        if pywaves.OFFLINE:
            return id
        elif id != -1:
            return pywaves.Order(id, assetPair, self)

    def sell(self, assetPair, amount, price, maxLifetime=30 * 86400, matcherFee=pywaves.DEFAULT_MATCHER_FEE, timestamp=0):
        id = self._postOrder(assetPair.asset1, assetPair.asset2, b'\1', amount, price, maxLifetime, matcherFee, timestamp)
        if pywaves.OFFLINE:
            return id
        elif id!=-1:
            return pywaves.Order(id, assetPair, self)

    def tradableBalance(self, assetPair):
        try:
            req = pywaves.wrapper('/matcher/orderbook/%s/%s/tradableBalance/%s' % ('WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId, self.address), host=pywaves.MATCHER)
            if pywaves.OFFLINE:
                    return req
            amountBalance = req['WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId]
            priceBalance = req['WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId]
        except:
            amountBalance = 0
            priceBalance = 0
        if not pywaves.OFFLINE:
            return amountBalance, priceBalance

    def lease(self, recipient, amount, txFee=pywaves.DEFAULT_LEASE_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif amount <= 0:
            msg = 'Amount must be > 0'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < amount + txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x08' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    base58.b58decode(bytes(recipient.address)) + \
                    struct.pack(">Q", amount) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "recipient": recipient.address,
                "amount": amount,
                "fee": txFee,
                "timestamp": timestamp,
                "signature": signature
            })
            req = pywaves.wrapper('/leasing/broadcast/lease', data)
            return req

    def leaseCancel(self, leaseId, txFee=pywaves.DEFAULT_LEASE_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x09' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp) + \
                    base58.b58decode(bytes(leaseId))
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "txId": leaseId,
                "fee": txFee,
                "timestamp": timestamp,
                "signature": signature
            })
            req = pywaves.wrapper('/leasing/broadcast/cancel', data)
            if pywaves.OFFLINE:
                return req
            elif 'leaseId' in req:
                return req['leaseId']

    def getOrderHistory(self, assetPair, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)
        sData = base58.b58decode(bytes(self.publicKey)) + \
                struct.pack(">Q", timestamp)
        signature = crypto.sign(self.privateKey, sData)
        data = {
            "Accept": "application/json",
            "Timestamp": bytes(timestamp),
            "Signature": signature
        }
        req = pywaves.wrapper('/matcher/orderbook/%s/%s/publicKey/%s' % ('WAVES' if assetPair.asset1.assetId=='' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId=='' else assetPair.asset2.assetId, self.publicKey), headers=data, host=pywaves.MATCHER)
        if 'message' in req:
            msg = req['message']
            logging.error(msg)
            pywaves.throw_error(msg)
        return req

    def cancelOpenOrders(self, assetPair):
        orders = self.getOrderHistory(assetPair)
        for order in orders:
            status = order['status']
            orderId = order['id']
            if status=='Accepted' or status=='PartiallyFilled':
                sData = base58.b58decode(bytes(self.publicKey)) + \
                        base58.b58decode(bytes(orderId))
                signature = crypto.sign(self.privateKey, sData)
                data = json.dumps({
                    "sender": self.publicKey,
                    "orderId": orderId,
                    "signature": signature
                })
                pywaves.wrapper('/matcher/orderbook/%s/%s/cancel' % ('WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)

    def deleteOrderHistory(self, assetPair):
        orders = self.getOrderHistory(assetPair)
        for order in orders:
            orderId = order['id']
            sData = base58.b58decode(bytes(self.publicKey)) + \
                    base58.b58decode(bytes(orderId))
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "sender": self.publicKey,
                "orderId": orderId,
                "signature": signature
            })
            pywaves.wrapper('/matcher/orderbook/%s/%s/delete' % ('WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)

    def createAlias(self, alias, txFee=pywaves.DEFAULT_ALIAS_FEE, timestamp=0):
        aliasWithNetwork = b'\x02' + crypto.str2bytes(bytes(pywaves.CHAIN_ID)) + struct.pack(">H", len(alias)) + crypto.str2bytes(alias)
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0a' + \
                    base58.b58decode(bytes(self.publicKey)) + \
                    struct.pack(">H", len(aliasWithNetwork)) + \
                    crypto.str2bytes(bytes(aliasWithNetwork)) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "alias": alias,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "signature": signature
            })
            return pywaves.wrapper('/alias/broadcast/create', data)

    def sponsorAsset(self, assetId, minimalFeeInAssets, txFee=pywaves.DEFAULT_SPONSOR_FEE, timestamp=0):
        if not self.privateKey:
            logging.error('Private key required')
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0e' + \
                b'\1' + \
                base58.b58decode(bytes(self.publicKey)) + \
                base58.b58decode(bytes(assetId)) + \
                struct.pack(">Q", minimalFeeInAssets) + \
                struct.pack(">Q", txFee) + \
                struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 14,
                "version": 1,
                "senderPublicKey": self.publicKey,
                "assetId": assetId,
                "fee": txFee,
                "timestamp": timestamp,
                "minSponsoredAssetFee": minimalFeeInAssets,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def setScript(self, scriptSource, txFee=pywaves.DEFAULT_SCRIPT_FEE, timestamp=0):
        script = pywaves.wrapper('/utils/script/compile', scriptSource)['script'][7:]
        if not self.privateKey:
            logging.error('Private key required')
        else:
            compiledScript = base64.b64decode(bytes(script))
            scriptLength = len(compiledScript)
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0d' + \
                b'\1' + \
                crypto.str2bytes(bytes(pywaves.CHAIN_ID)) + \
                base58.b58decode(bytes(self.publicKey)) + \
                b'\1' + \
                struct.pack(">H", scriptLength) + \
                compiledScript + \
                struct.pack(">Q", txFee) + \
                struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 13,
                "version": 1,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "script": 'base64:' + script,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def setAssetScript(self, asset, scriptSource, txFee=pywaves.DEFAULT_ASSET_SCRIPT_FEE, timestamp=0):
        script = pywaves.wrapper('/utils/script/compile', scriptSource)['script'][7:]
        if not self.privateKey:
            logging.error('Private key required')
        else:
            compiledScript = base64.b64decode(script)
            scriptLength = len(compiledScript)
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0f' + \
                b'\1' + \
                crypto.str2bytes(str(pywaves.CHAIN_ID)) + \
                base58.b58decode(self.publicKey) + \
                base58.b58decode(asset.assetId) + \
                struct.pack(">Q", txFee) + \
                struct.pack(">Q", timestamp) + \
                b'\1' + \
                struct.pack(">H", scriptLength) + \
                compiledScript
            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 15,
                "version": 1,
                "assetId": asset.assetId,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "script": 'base64:' + script,
                "proofs": [
                    signature
                ]
            })
            print(data)

            return pywaves.wrapper('/transactions/broadcast', data)

    def issueSmartAsset(self, name, description, quantity, scriptSource, decimals=0, reissuable=False, txFee=pywaves.DEFAULT_ASSET_FEE):
        script = pywaves.wrapper('/utils/script/compile', scriptSource)['script'][7:]
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif len(name) < 4 or len(name) > 16:
            msg = 'Asset name must be between 4 and 16 characters long'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            compiledScript = base64.b64decode(script)
            scriptLength = len(compiledScript)
            timestamp = int(time.time() * 1000)
            sData = b'\3' + \
                    b'\2' + \
                    crypto.str2bytes(str(pywaves.CHAIN_ID)) + \
                    base58.b58decode(self.publicKey) + \
                    struct.pack(">H", len(name)) + \
                    crypto.str2bytes(name) + \
                    struct.pack(">H", len(description)) + \
                    crypto.str2bytes(description) + \
                    struct.pack(">Q", quantity) + \
                    struct.pack(">B", decimals) + \
                    (b'\1' if reissuable else b'\0') + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp) + \
                    b'\1' + \
                    struct.pack(">H", scriptLength) + \
                    compiledScript
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "type": 3,
                "senderPublicKey": self.publicKey,
                "name": name,
                "version": 2,
                "quantity": quantity,
                "timestamp": timestamp,
                "description": description,
                "decimals": decimals,
                "reissuable": reissuable,
                "fee": txFee,
                "proofs": [ signature ],
                "script": 'base64:' + script
            })
            print(data)
            req = pywaves.wrapper('/transactions/broadcast', data)
            if pywaves.OFFLINE:
                return req
            else:
                return req
