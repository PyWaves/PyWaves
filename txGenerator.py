import pywaves

class TxGenerator:

    def generateSendWaves(self, recipient, amount, publicKey, attachment='', txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 4,
            "version": 2,
            "senderPublicKey": publicKey,
            "recipient": recipient.address,
            "amount": amount,
            "fee": txFee,
            "timestamp": timestamp,
            "attachment": attachment,
            "proofs": []
        }

        return tx

    def generateSendAsset(self, recipient, asset, amount, publicKey, attachment='', feeAsset='', txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        if (feeAsset != '' and feeAsset != None):
            feeAsset = feeAsset.assetId
        asset = asset.assetId
        tx = {
            "version": 2,
            "type": 4,
            "assetId": asset,
            "feeAssetId": (feeAsset if feeAsset != '' else None),
            "senderPublicKey": publicKey,
            "recipient": recipient.address,
            "amount": amount,
            "fee": txFee,
            "timestamp": timestamp,
            "attachment": attachment,
            "proofs": [ ]
        }

        return tx