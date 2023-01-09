import base58
import base64
import struct
import pywaves.crypto as crypto
import pywaves as pw

from .protobuf import transaction_pb2
from .protobuf.waves import amount_pb2

class TxSigner:

    def signTx(self, tx, privateKey):
        if tx['type'] == 3 and 'script' in tx:
            self.signType03SmartTx(tx, privateKey)
        elif tx['type'] == 3:
            self.signType03Tx(tx, privateKey)
        elif tx['type'] == 4 and ('assetId' not in tx or tx['assetId'] == None):
            self.signType04WavesTx(tx, privateKey)
        elif tx['type'] == 4 and ('assetId' in tx and tx['assetId'] != None):
            self.signType04AssetTx(tx, privateKey)
        elif tx['type'] == 5:
            self.signType05Tx(tx, privateKey)
        elif tx['type'] == 6:
            self.signType06Tx(tx, privateKey)
        elif tx['type'] == 8:
            self.signType08Tx(tx, privateKey)
        elif tx['type'] == 9:
            self.signType09Tx(tx, privateKey)
        elif tx['type'] == 10:
            self.signType10Tx(tx, privateKey)
        elif tx['type'] == 11 and ('assetId' not in tx or tx['assetId'] == None or tx['assetId'] == ''):
            self.signType11TxWaves(tx, privateKey)
        elif tx['type'] == 11 and ('assetId' in tx and tx['assetId'] != None):
            self.signType11TxAssets(tx, privateKey)
        elif tx['type'] == 12 and (tx['data'][0]['value'] == None):
            self.signType12DeleteTx(tx, privateKey)
        elif tx['type'] == 12:
            self.signType12Tx(tx, privateKey)
        elif tx['type'] == 13:
            self.signType13Tx(tx, privateKey)
        elif tx['type'] == 14:
            self.signType14Tx(tx, privateKey)
        elif tx['type'] == 15:
            self.signType15Tx(tx, privateKey)
        elif tx['type'] == 16:
            self.signType16Tx(tx, privateKey)
        elif tx['type'] == 17:
            self.signType17Tx(tx, privateKey)

    def signType04WavesTx(self, tx, privateKey):
        sData = b'\4' + \
                b'\2' + \
                base58.b58decode(tx['senderPublicKey']) + \
                b'\0\0' + \
                struct.pack(">Q", tx['timestamp']) + \
                struct.pack(">Q", tx['amount']) + \
                struct.pack(">Q", tx['fee']) + \
                base58.b58decode(tx['recipient']) + \
                struct.pack(">H", len(base58.b58decode(tx['attachment']))) + \
                base58.b58decode(tx['attachment'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType04AssetTx(self, tx, privateKey):
        sData = b'\4' + \
                b'\2' + \
                base58.b58decode(tx['senderPublicKey']) + \
                b'\1' + base58.b58decode(tx['assetId']) + \
                (b'\1' + base58.b58decode(tx['feeAssetId']) if ('feeAssetId' in tx and tx['feeAssetId'] != None and tx['feeAssetId'] != '') else b'\0') + \
                struct.pack(">Q", tx['timestamp']) + \
                struct.pack(">Q", tx['amount']) + \
                struct.pack(">Q", tx['fee']) + \
                base58.b58decode(tx['recipient']) + \
                struct.pack(">H", len(base58.b58decode(tx['attachment']))) + \
                base58.b58decode(tx['attachment'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType03Tx(self, tx, privateKey):
        sData = b'\3' + \
                base58.b58decode(tx['senderPublicKey']) + \
                struct.pack(">H", len(tx['name'])) + \
                crypto.str2bytes(tx['name']) + \
                struct.pack(">H", len(tx['description'])) + \
                crypto.str2bytes(tx['description']) + \
                struct.pack(">Q", tx['quantity']) + \
                struct.pack(">B", tx['decimals']) + \
                (b'\1' if tx['reissuable'] else b'\0') + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType03SmartTx(self, tx, privateKey):
        compiledScript = base64.b64decode(tx['script'][7:])
        scriptLength = len(compiledScript)

        sData = b'\3' + \
                b'\2' + \
                crypto.str2bytes(str(pw.CHAIN_ID)) + \
                base58.b58decode(tx['senderPublicKey']) + \
                struct.pack(">H", len(tx['name'])) + \
                crypto.str2bytes(tx['name']) + \
                struct.pack(">H", len(tx['description'])) + \
                crypto.str2bytes(tx['description']) + \
                struct.pack(">Q", tx['quantity']) + \
                struct.pack(">B", tx['decimals']) + \
                (b'\1' if tx['reissuable'] else b'\0') + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp']) + \
                b'\1' + \
                struct.pack(">H", scriptLength) + \
                compiledScript

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType05Tx(self, tx, privateKey):
        sData = b'\5' + \
                base58.b58decode(tx['senderPublicKey']) + \
                base58.b58decode(tx['assetId']) + \
                struct.pack(">Q", tx['quantity']) + \
                (b'\1' if tx['reissuable'] else b'\0') + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType06Tx(self, tx, privateKey):
        sData = '\6' + \
                crypto.bytes2str(base58.b58decode(tx['senderPublicKey'])) + \
                crypto.bytes2str(base58.b58decode(tx['assetId'])) + \
                crypto.bytes2str(struct.pack(">Q", tx['quantity'])) + \
                crypto.bytes2str(struct.pack(">Q", tx['fee'])) + \
                crypto.bytes2str(struct.pack(">Q", tx['timestamp']))

        proof = crypto.sign(privateKey, crypto.str2bytes(sData))
        tx['proofs'].append(proof)

    def signType08Tx(self, tx, privateKey):
        sData = b'\x08' + \
                b'\x02' + \
                b'\x00' + \
                base58.b58decode(tx['senderPublicKey']) + \
                base58.b58decode(tx['recipient']) + \
                struct.pack(">Q", tx['amount']) + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType09Tx(self, tx, privateKey):
        sData = b'\x09' + \
                base58.b58decode(tx['senderPublicKey']) + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp']) + \
                base58.b58decode(tx['txId'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType10Tx(self, tx, privateKey):
        aliasWithNetwork = b'\x02' + crypto.str2bytes(str(pw.CHAIN_ID)) + struct.pack(">H", len(tx['alias'])) + crypto.str2bytes(tx['alias'])
        sData = b'\x0a' + \
                base58.b58decode(tx['senderPublicKey']) + \
                struct.pack(">H", len(aliasWithNetwork)) + \
                aliasWithNetwork + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType11TxWaves(self, tx, privateKey):
        transfers = tx['transfers']
        transfersData = b''
        for i in range(0, len(transfers)):
            transfersData += base58.b58decode(transfers[i]['recipient']) + struct.pack(">Q", transfers[i]['amount'])
        sData = b'\x0b' + \
                b'\1' + \
                base58.b58decode(tx['senderPublicKey']) + \
                b'\0' + \
                struct.pack(">H", len(transfers)) + \
                transfersData + \
                struct.pack(">Q", tx['timestamp']) + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">H", len(base58.b58decode(tx['attachment']))) + \
                base58.b58decode(tx['attachment'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType11TxAssets(self, tx, privateKey):
        transfers = tx['transfers']
        transfersData = b''
        for i in range(0, len(transfers)):
            transfersData += base58.b58decode(transfers[i]['recipient']) + struct.pack(">Q", transfers[i]['amount'])

        sData = b'\x0b' + \
            b'\1' + \
            base58.b58decode(tx['senderPublicKey']) + \
            b'\1' + \
            base58.b58decode(tx['assetId']) + \
            struct.pack(">H", len(tx['transfers'])) + \
            transfersData + \
            struct.pack(">Q", tx['timestamp']) + \
            struct.pack(">Q", tx['fee']) + \
            struct.pack(">H", len(base58.b58decode(tx['attachment']))) + \
            base58.b58decode(tx['attachment'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType12DeleteTx(self, tx, privateKey):
        dataTransaction = transaction_pb2.DataTransactionData()

        entry = transaction_pb2.DataTransactionData.DataEntry()

        entry.key = tx['data'][0]['key']
        dataTransaction.data.append(entry)

        txFee = amount_pb2.Amount()
        txFee.amount = tx['fee']
        transaction = transaction_pb2.Transaction()
        transaction.chain_id = ord(pw.CHAIN_ID)
        transaction.sender_public_key = base58.b58decode(tx['senderPublicKey'])
        transaction.fee.CopyFrom(txFee)
        transaction.timestamp = tx['timestamp']
        transaction.version = tx['version']
        transaction.data_transaction.CopyFrom(dataTransaction)

        proof = crypto.sign(privateKey, transaction.SerializeToString())
        tx['proofs'].append(proof)

    def signType12Tx(self, tx, privateKey):
        dataTransaction = transaction_pb2.DataTransactionData()

        for d in tx['data']:
            entry = transaction_pb2.DataTransactionData.DataEntry()
            if d['type'] == 'boolean':
                entry.key = d['key']
                entry.bool_value = d['value']
            elif d['type'] == 'string':
                entry.key = d['key']
                entry.string_value = d['value']
            elif d['type'] == 'integer':
                entry.key = d['key']
                entry.int_value = d['value']
            elif d['type'] == 'binary':
                entry.key = d['key']
                entry.binary_value = base64.b64decode(d['value'][7:])
            dataTransaction.data.append(entry)

        txFee = amount_pb2.Amount()
        txFee.amount = tx['fee']
        transaction = transaction_pb2.Transaction()
        transaction.chain_id = ord(pw.CHAIN_ID)
        transaction.sender_public_key = base58.b58decode(tx['senderPublicKey'])
        transaction.fee.CopyFrom(txFee)
        transaction.timestamp = tx['timestamp']
        transaction.version = tx['version']
        transaction.data_transaction.CopyFrom(dataTransaction)

        proof = crypto.sign(privateKey, transaction.SerializeToString())
        tx['proofs'].append(proof)

    def signType14Tx(self, tx, privateKey):
        sData = b'\x0e' + \
                b'\1' + \
                base58.b58decode(tx['senderPublicKey']) + \
                base58.b58decode(tx['assetId']) + \
                struct.pack(">Q", tx['minSponsoredAssetFee']) + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType13Tx(self, tx, privateKey):
        setScriptTransaction = transaction_pb2.SetScriptTransactionData()
        setScriptTransaction.script = base64.b64decode(tx['script'])
        tx_fee = amount_pb2.Amount()
        tx_fee.amount = tx['fee']
        transaction = transaction_pb2.Transaction()
        transaction.chain_id = ord(pw.CHAIN_ID)
        transaction.sender_public_key = base58.b58decode(tx['senderPublicKey'])
        transaction.fee.CopyFrom(tx_fee)
        transaction.timestamp = tx['timestamp']
        transaction.version = 2
        transaction.set_script.CopyFrom(setScriptTransaction)

        proof = crypto.sign(privateKey, transaction.SerializeToString())
        tx['proofs'].append(proof)

    def signType15Tx(self, tx, privateKey):
        compiledScript = base64.b64decode(tx['script'][7:])
        scriptLength = len(compiledScript)
        sData = b'\x0f' + \
                b'\1' + \
                crypto.str2bytes(str(pw.CHAIN_ID)) + \
                base58.b58decode(tx['senderPublicKey']) + \
                base58.b58decode(tx['assetId']) + \
                struct.pack(">Q", tx['fee']) + \
                struct.pack(">Q", tx['timestamp']) + \
                b'\1' + \
                struct.pack(">H", scriptLength) + \
                compiledScript

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType17Tx(self, tx, privateKey):
        decodedAssetId = base58.b58decode(tx['assetId'])
        updateInfo = transaction_pb2.UpdateAssetInfoTransactionData()
        updateInfo.asset_id = decodedAssetId
        updateInfo.name = tx['name']
        updateInfo.description = tx['description']
        txFee = amount_pb2.Amount()
        txFee.amount = tx['fee']
        transaction = transaction_pb2.Transaction()
        transaction.chain_id = ord(pw.CHAIN_ID)
        transaction.sender_public_key = base58.b58decode(tx['senderPublicKey'])
        transaction.fee.CopyFrom(txFee)
        transaction.timestamp = tx['timestamp']
        transaction.version = 1
        transaction.update_asset_info.CopyFrom(updateInfo)

        proof = crypto.sign(privateKey, transaction.SerializeToString())
        tx['proofs'].append(proof)

    def signType16Tx(self, tx, privateKey):
        functionFlag = b'\x01'
        parameterBytes = b''
        for param in tx['call']['args']:
            if param['type'] == 'integer':
                parameterBytes += b'\0' + struct.pack(">q", param['value'])
            elif param['type'] == 'binary':
                parameterBytes += b'\1' + struct.pack(">L", len(param['value'])) + crypto.str2bytes(param['value'])
            elif param['type'] == 'string':
                parameterBytes += b'\2' + struct.pack(">I", len(crypto.str2bytes(param['value']))) + crypto.str2bytes(
                    param['value'])
            elif param['type'] == 'boolean':
                if param['value'] == True:
                    parameterBytes += b'\6'
                else:
                    parameterBytes += b'\7'
            elif param['type'] == 'list':
                parameterBytes += b'\x0b'
                parameterBytes += struct.pack(">I", len(param['value']))
                for nestedParam in param['value']:
                    if nestedParam['type'] == 'integer':
                        parameterBytes += b'\0' + struct.pack(">Q", nestedParam['value'])
                    elif nestedParam['type'] == 'binary':
                        parameterBytes += b'\1' + struct.pack(">I", len(nestedParam['value'])) + crypto.str2bytes(nestedParam['value'])
                    elif nestedParam['type'] == 'string':
                        parameterBytes += b'\2' + struct.pack(">I", len(crypto.str2bytes(
                            nestedParam['value']))) + crypto.str2bytes(nestedParam['value'])
                    elif nestedParam['type'] == 'boolean':
                        if nestedParam['value'] == True:
                            parameterBytes += b'\6'
                        else:
                            parameterBytes += b'\7'
        paymentBytes = b''
        for payment in tx['payment']:
            currentPaymentBytes = b''
            if ('assetId' in payment and payment['assetId'] != None and payment['assetId'] != ''):
                currentPaymentBytes += struct.pack(">Q", payment['amount']) + b'\x01' + base58.b58decode(
                    payment['assetId'])
            else:
                currentPaymentBytes += struct.pack(">Q", payment['amount']) + b'\x00'
            paymentBytes += struct.pack(">H", len(currentPaymentBytes)) + currentPaymentBytes
        assetIdBytes = b''
        if (tx['feeAssetId']):
            assetIdBytes += b'\x01' + base58.b58decode(tx['feeAssetId'])
        else:
            assetIdBytes += b'\x00'

        if tx['call']['function'] is None:
            sData = b'\x10' + \
                    b'\x01' + \
                    crypto.str2bytes(str(pw.CHAIN_ID)) + \
                    base58.b58decode(tx['senderPublicKey']) + \
                    base58.b58decode(tx['dApp']) + \
                    b'\x00' + \
                    struct.pack(">H", len(tx['payment'])) + \
                    paymentBytes + \
                    struct.pack(">Q", tx['fee']) + \
                    assetIdBytes + \
                    struct.pack(">Q", tx['timestamp'])
        else:
            sData = b'\x10' + \
                    b'\x01' + \
                    crypto.str2bytes(str(pw.CHAIN_ID)) + \
                    base58.b58decode(tx['senderPublicKey']) + \
                    base58.b58decode(tx['dApp']) + \
                    b'\x01' + \
                    b'\x09' + \
                    b'\x01' + \
                    struct.pack(">L", len(crypto.str2bytes(tx['call']['function']))) + \
                    crypto.str2bytes(tx['call']['function']) + \
                    struct.pack(">I", len(tx['call']['args'])) + \
                    parameterBytes + \
                    struct.pack(">H", len(tx['payment'])) + \
                    paymentBytes + \
                    struct.pack(">Q", tx['fee']) + \
                    assetIdBytes + \
                    struct.pack(">Q", tx['timestamp'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)




