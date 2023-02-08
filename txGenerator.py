import pywaves
import pywaves.crypto as crypto
import time
import json
import base64
import base58

class TxGenerator:

    def __init__(self, pywaves=pywaves):
        self.pywaves = pywaves

    def generateSendWaves(self, recipient, amount, publicKey, attachment='', txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        attachment = base58.b58encode(crypto.str2bytes(attachment))
        tx = {
            "type": 4,
            "version": 3,
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
        attachment = base58.b58encode(crypto.str2bytes(attachment))
        tx = {
            "version": 3,
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

    def generateIssueAsset(self, name, description, quantity, publicKey, decimals=0, reissuable=False, txFee=pywaves.DEFAULT_ASSET_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "version": 3, #1
            "type": 3,
            "senderPublicKey": publicKey,
            "name": name,
            "quantity": quantity,
            "timestamp": timestamp,
            "description": description,
            "decimals": decimals,
            "reissuable": reissuable,
            "fee": txFee,
            "proofs": []
        }

        return tx

    def generateIssueSmartAsset(self, name, description, quantity, scriptSource, publicKey, decimals=0, reissuable=False, txFee=pywaves.DEFAULT_ASSET_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        script = self.pywaves.wrapper('/utils/script/compileCode', scriptSource)['script'][7:]
        tx = {
            "type": 3,
            "senderPublicKey": publicKey,
            "name": name,
            "version": 3,
            "quantity": quantity,
            "timestamp": timestamp,
            "description": description,
            "decimals": decimals,
            "reissuable": reissuable,
            "fee": txFee,
            "proofs": [ ],
            "script": 'base64:' + script
        }

        return tx

    def generateReissueAsset(self, asset, quantity, publicKey, reissuable=False, txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 5,
            "senderPublicKey": publicKey,
            "assetId": asset.assetId,
            "quantity": quantity,
            "timestamp": timestamp,
            "reissuable": reissuable,
            "fee": txFee,
            "proofs": [],
            "version": 3
        }

        return tx

    def generateBurnAsset(self, asset, quantity, publicKey, txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 6,
            "senderPublicKey": publicKey,
            "assetId": asset.assetId,
            "quantity": quantity,
            "timestamp": timestamp,
            "fee": txFee,
            "proofs": [],
            "version": 3
        }

        return tx

    def generateMassTransferWaves(self, transfers, publicKey, attachment='', timestamp=0, txFee=pywaves.DEFAULT_BASE_FEE):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)
        attachment = base58.b58encode(crypto.str2bytes(attachment))

        tx = {
            "type": 11,
            "version": 2,
            "assetId": "",
            "senderPublicKey": publicKey,
            "fee": txFee,
            "timestamp": timestamp,
            "transfers": transfers,
            "attachment": attachment,
            "proofs": [ ]
        }

        return tx

    def generateMassTransferAssets(self, transfers, asset, publicKey, attachment='', timestamp=0, txFee=pywaves.DEFAULT_BASE_FEE):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)
        attachment = base58.b58encode(crypto.str2bytes(attachment))

        tx = {
            "type": 11,
            "version": 2,
            "assetId": asset.assetId,
            "senderPublicKey": publicKey,
            "fee": txFee,
            "timestamp": timestamp,
            "transfers": transfers,
            "attachment": attachment,
            "proofs": [ ]
        }

        return tx

    def generateLease(self, recipient, amount, publicKey, txFee=pywaves.DEFAULT_LEASE_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 8,
            "senderPublicKey": publicKey,
            "recipient": recipient.address,
            "amount": amount,
            "fee": txFee,
            "timestamp": timestamp,
            "proofs": [ ],
            "version": 3 #2
        }

        return tx

    def generateLeaseCancel(self, leaseId, publicKey, txFee=pywaves.DEFAULT_LEASE_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 9,
            "senderPublicKey": publicKey,
            "txId": leaseId,
            "fee": txFee,
            "timestamp": timestamp,
            "proofs": [ ],
            "version": 3
        }

        return tx

    def generateAlias(self, alias, publicKey, txFee=pywaves.DEFAULT_ALIAS_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 10,
            "alias": alias,
            "senderPublicKey": publicKey,
            "fee": txFee,
            "timestamp": timestamp,
            "proofs": [],
            "version": 3 #1
        }

        return tx

    def generateSponsorAsset(self, assetId, minimalFeeInAssets, publicKey, txFee=pywaves.DEFAULT_SPONSOR_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 14,
            "version": 2, #1
            "senderPublicKey": publicKey,
            "assetId": assetId,
            "fee": txFee,
            "timestamp": timestamp,
            "minSponsoredAssetFee": minimalFeeInAssets,
            "proofs": [ ]
        }

        return tx

    def generateSetScript(self, script, publicKey, txFee=pywaves.DEFAULT_SCRIPT_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            "type": 13,
            "proofs": [],
            "senderPublicKey": publicKey,
            "fee": txFee,
            "timestamp": timestamp,
            "chainId": ord(self.pywaves.CHAIN_ID),
            "version": 2,
            "script": script
        }

        return tx

    def generateDatatransaction(self, data, publicKey, timestamp=0, baseFee=pywaves.DEFAULT_BASE_FEE, minimalFee=500000):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        dataList = []
        for d in data:
            listEntry = {}
            if d['type'] == 'boolean':
                listEntry['key'] = d['key']
                listEntry['value'] = d['value']
                listEntry['type'] = 'boolean'
            elif d['type'] == 'string':
                listEntry['key'] = d['key']
                listEntry['value'] = d['value']
                listEntry['type'] = 'string'
            elif d['type'] == 'integer':
                listEntry['key'] = d['key']
                listEntry['value'] = d['value']
                listEntry['type'] = 'integer'
            elif d['type'] == 'binary':
                listEntry['key'] = d['key']
                base64Encoded = base64.b64encode(crypto.str2bytes(d['value']))
                listEntry['value'] = 'base64:' + crypto.bytes2str(base64Encoded)
                listEntry['type'] = 'binary'
            dataList.append(listEntry)

        txFeeAmount = (int(((len(crypto.str2bytes(json.dumps(data))) + 2 + 64)) / 1000.0) + 1) * baseFee
        txFeeAmount = max(txFeeAmount, minimalFee)

        tx = {
            "type": 12,
            "proofs": [],
            "senderPublicKey": publicKey,
            "fee": txFeeAmount,
            "timestamp": timestamp,
            "chainId": ord(self.pywaves.CHAIN_ID),
            "versoin": 2,
            "data": dataList,
            "version": 2
        }

        return tx

    def generateDeleteDataEntry(self, key, publicKey, timestamp=0, minimalFee=500000):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        dataList = []
        listEntry = {}

        listEntry['key'] = key
        listEntry['value'] = None
        listEntry['type'] = None
        dataList.append(listEntry)

        tx = {
            "type": 12,
            "proofs": [],
            "senderPublicKey": publicKey,
            "fee": minimalFee,
            "timestamp": timestamp,
            "chainId": ord(self.pywaves.CHAIN_ID),
            "version": 2,
            "data": dataList
        }

        return tx

    def generateSetAssetScript(self, asset, scriptSource, publicKey, txFee=pywaves.DEFAULT_ASSET_SCRIPT_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        script = self.pywaves.wrapper('/utils/script/compile', scriptSource)['script'][7:]
        tx = {
            "type": 15,
            "version": 2, #1,
            "assetId": asset.assetId,
            "senderPublicKey": publicKey,
            "fee": txFee,
            "timestamp": timestamp,
            "script": 'base64:' + script,
            "proofs": [ ]
        }

        return tx

    def generateUpdateAssetInfo(self, assetId, name, description, publicKey, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)

        tx = {
            'type': 17,
            'assetId': assetId,
            'proofs': [],
            'senderPublicKey': publicKey,
            'fee': 1000000,
            'timestamp': timestamp,
            'chainId': ord(self.pywaves.CHAIN_ID),
            'version': 1,
            'name': name,
            'description': description
        }

        return tx

    def generateInvokeScript(self, dappAddress, functionName, publicKey, params = [], payments = [], feeAsset=None, txFee=pywaves.DEFAULT_INVOKE_SCRIPT_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)
        tx = {
            "type": 16,
            "senderPublicKey": publicKey,
            "version": 2,
            "timestamp": timestamp,
            "fee": txFee,
            "proofs": [],
            "feeAssetId": feeAsset,
            "dApp": dappAddress,
            "payment": payments
        }

        if functionName is not None:
            tx['call'] = {
                "function": functionName,
                "args": params
            }

        return tx