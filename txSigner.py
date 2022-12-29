import base58
import struct
import pywaves.crypto as crypto

class TxSigner:

    def signTx(self, tx, privateKey):
        if tx['type'] == 4 and ('assetId' not in tx or tx['assetId'] == None):
            self.signType04WavesTx(tx, privateKey)
        if tx['type'] == 4 and ('assetId' in tx and tx['assetId'] != None):
            self.signType04AssetTx(tx, privateKey)

    def signType04WavesTx(self, tx, privateKey):
        sData = b'\4' + \
                b'\2' + \
                base58.b58decode(tx['senderPublicKey']) + \
                b'\0\0' + \
                struct.pack(">Q", tx['timestamp']) + \
                struct.pack(">Q", tx['amount']) + \
                struct.pack(">Q", tx['fee']) + \
                base58.b58decode(tx['recipient']) + \
                struct.pack(">H", len(tx['attachment'])) + \
                crypto.str2bytes(tx['attachment'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)

    def signType04AssetTx(self, tx, privateKey):
        print(tx['feeAssetId'])
        sData = b'\4' + \
                b'\2' + \
                base58.b58decode(tx['senderPublicKey']) + \
                b'\1' + base58.b58decode(tx['assetId']) + \
                (b'\1' + base58.b58decode(tx['feeAssetId']) if ('feeAssetId' in tx and tx['feeAssetId'] != None and tx['feeAssetId'] != '') else b'\0') + \
                struct.pack(">Q", tx['timestamp']) + \
                struct.pack(">Q", tx['amount']) + \
                struct.pack(">Q", tx['fee']) + \
                base58.b58decode(tx['recipient']) + \
                struct.pack(">H", len(tx['attachment'])) + \
                crypto.str2bytes(tx['attachment'])

        proof = crypto.sign(privateKey, sData)
        tx['proofs'].append(proof)
