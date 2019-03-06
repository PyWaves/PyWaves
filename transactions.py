from collections import OrderedDict


class Transaction(OrderedDict):
    def __init__(self, *args, **kwargs):
        OrderedDict.__init__(self, *args, **kwargs)

    def pack(self):
        from crypto import str2bytes
        from struct import pack as spack
        from base58 import b58decode
        data = b''
        for key, value in self.iteritems():
            if key == 'signature' or key == 'proofs':
                continue
            elif key == 'type' or key == 'version' or key == 'decimals' or key == 'reissuable':
                data += spack('>B', value)
            elif key == 'attachment' or key == 'name' or key == 'description':
                data += spack('>H', len(value)) + str2bytes(value)
            elif key == 'timestamp' or key == 'amount' or key == 'fee' or key == 'quantity':
                data += spack('>Q', value)
            elif key == 'assetId' or key == 'feeAssetId':
                    data += (b'\1' + b58decode(bytes(value)) if value else b'\0')
            elif key == 'senderPublicKey' or key == 'recipient' or key == 'txId':
                data += b58decode(bytes(value))
            elif key == 'transfers':
                data += spack(">H", len(value))
                for transfer in value:
                    data += b58decode(bytes(t['recipient']) + spack(">Q", t['amount']))
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


def generate_method(type_id, argnames):
    def payload(*args):
        tx = Transaction()
        tx['type'] = 3
        for i, arg in enumerate(argnames):
            tx[arg] = args[i]
        tx['proofs'] = []
        return tx
    return payload


issue = generate_method(3, ['senderPublicKey', 'name', 'description', 'quantity', 'decimals', 'reissuable', 'fee', 'timestamp'])
transfer = generate_method(4, ['senderPublicKey', 'assetId', 'feeAssetId', 'timestamp', 'amount', 'fee', 'recipient', 'attachment'])
reissue = generate_method(5, ['senderPublicKey', 'assetId', 'quantity', 'reissuable', 'fee', 'timestamp'])
burn = generate_method(6, ['senderPublicKey', 'assetId', 'quantity', 'fee', 'timestamp'])
#  exchange = generate_method(7, ...)
lease = generate_method(8, ['senderPublicKey', 'recipient', 'amount', 'fee', 'timestamp'])
leaseCancel = generate_method(9, ['senderPublicKey', 'fee', 'timestamp', 'txId'])
alias = generate_method(10, ['senderPublicKey', 'alias', 'fee', 'timestamp'])
massTransfer = generate_method(11, ['version', 'senderPublicKey', 'version', 'assetId', 'transfers', 'timestamp', 'fee', 'attachment'])
data = generate_method(12, ['version', 'senderPublicKey', 'data', 'timestamp', 'fee'])
"""
setScript = generate_method(13
sponsorFee = generate_method(14
setAssetScript = generate_method(15
contractInvocation = generate_method(16
"""
