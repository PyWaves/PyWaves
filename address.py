import base58
import sha3
import pyblake2
import axolotl_curve25519 as curve

def hashChain(s):
    b = pyblake2.blake2b(s, digest_size=32).digest()
    return sha3.keccak_256(b).digest()

CHAIN_ID = 'W'

a="FwwzYrvQ3ur8Yd8HehXLt7syEcdEQLBFSoVT9yecZ6eP"
privateKey=a
privKey = base58.b58decode(privateKey)
pubKey = curve.generatePublicKey(privKey)
pubKey="26pTTB2xQ4LBXsmix9gXsC4MSRYKQeUyJrR9i5U2ParA"
unhashedAddress = chr(1) + CHAIN_ID + hashChain(pubKey)[0:20]
addressHash = hashChain(unhashedAddress)[0:4]
address = base58.b58encode(unhashedAddress + addressHash)

print address


