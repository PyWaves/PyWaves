from collections import OrderedDict


class Transaction(OrderedDict):
    def __init__(self, *args, **kwargs):
        OrderedDict.__init__(self, *args, **kwargs)

    def pack(self):
        from crypto import str2bytes
        from struct import pack as spack
        from base58 import b58decode
        data = ''
        for key, value in self.iteritems():
            if key == 'signature' or key == 'proofs':
                continue
            elif key == 'type' or key == 'decimals' or key == 'reissuable':
                data += spack('>B', value)
            elif key == 'attachment' or key == 'name' or key == 'description':
                data += spack('>H', len(value)) + str2bytes(value)
            elif key == 'timestamp' or key == 'amount' or key == 'fee' or key == 'quantity':
                data += spack('>Q', value)
            elif key == 'assetId' or key == 'feeAssetId':
                data += (b'\1' + b58decode(bytes(value)) if value else b'\0')
            elif key == 'senderPublicKey' or key == 'recipient':
                data += b58decode(bytes(value))
            else:
                raise Exception('unknown tx field "{}"'.format(key))
        return data

    def sign(self, privateKey):
        from crypto import sign as csign
        result = csign(privateKey, self.pack())
        if 'proofs' in self:
            if isinstance(self['proofs'], list):
                self['proofs'].append(result)
            else:
                self['proofs'] = [ result ]
        else:
            self['signature'] = result
        return result

    def json(self):
        from json import dumps
        return dumps(self)


def transfer(senderPublicKey, assetId, feeAssetId, timestamp, amount, fee, recipient, attachment):
    tx = Transaction()
    tx['type'] = 4
    tx['senderPublicKey'] = senderPublicKey
    tx['assetId'] = assetId
    tx['feeAssetId'] = feeAssetId
    tx['timestamp'] = timestamp
    tx['amount'] = amount
    tx['fee'] = fee
    tx['recipient'] = recipient
    tx['attachment'] = attachment
    tx['proofs'] = None
    return tx

