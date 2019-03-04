from collections import OrderedDict


def pack(tx):
    from struct import pack as spack
    from base58 import b58decode
    data = ''
    for key, value in tx.iteritems():
        if key == 'type' or key == 'decimals' or key == 'reissuable':
            data += spack('>B', value)
        elif key == 'attachment' or key == 'name' or key == 'description':
            data += spack('>H', len(value)) + crypto.str2bytes(value)
        elif key == 'timestamp' or key == 'amount' or key == 'fee' or key == 'quantity':
            data += spack('>Q', value)
        elif key == 'assetId' or key == 'feeAssetId':
            data += (b'\1' + b58decode(bytes(value)) if value else b'\0')
        elif key == 'senderPublicKey' or key == 'recipient':
            data += b58decode(bytes(value))
        else:
            raise Exception('unknown tx field "{}"'.format(key))
    return data


def sign(privateKey, tx):
    from crypto import sign as csign
    return csign(privateKey, pack(tx))


def transfer(senderPublicKey, assetId, feeAssetId, timestamp, amount, fee, recipient, attachment):
    tx = OrderedDict()
    tx['type'] = 4
    tx['senderPublicKey'] = senderPublicKey
    tx['assetId'] = assetId
    tx['feeAssetId'] = feeAssetId
    tx['timestamp'] = timestamp
    tx['amount'] = amount
    tx['fee'] = fee
    tx['recipient'] = recipient
    tx['attachment'] = attachment
    return tx

