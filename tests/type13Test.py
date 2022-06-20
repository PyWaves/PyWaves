from .. import pywaves as pw
from .. import address
from .. import asset
from .. import order
import pytest
from .helpers import Helpers
import time

pw.setThrowOnError(True)

def test_setScriptWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    scriptSource =  '{-# STDLIB_VERSION 5 #-}\n' \
                    '{-# CONTENT_TYPE DAPP #-}\n' \
                    '{-# SCRIPT_TYPE ACCOUNT #-}\n'\
                    '\n' \
                    '@Callable(i)\n' \
                    'func storeValue(name: String, value: Int) = {\n'\
                      '[ IntegerEntry(name, value) ]\n'\
                    '}\n'\
                    '\n'\
                    '@Verifier(tx)\n'\
                    'func verify() = sigVerify(tx.bodyBytes, tx.proofs[0], tx.senderPublicKey)'


    with pytest.raises(Exception) as error:
        myAddress.setScript(scriptSource)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_succesfullSetScript():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    script ='{-# STDLIB_VERSION 5 #-}\n' \
            '{-# CONTENT_TYPE DAPP #-}\n' \
            '{-# SCRIPT_TYPE ACCOUNT #-}\n' \
            '\n' \
            '@Callable(i)\n' \
            'func storeValue(name: String, value: Int) = {\n' \
            '[ IntegerEntry(name, value) ]\n' \
            '}\n' \
            '\n' \
            '@Verifier(tx)\n' \
            'func verify() = sigVerify(tx.bodyBytes, tx.proofs[0], tx.senderPublicKey)\n' \
            '\n' \
            '@Callable(i)\n' \
            'func storeListValue(name: String, value1: List[String], value2: List[Int], value3: List[Boolean]) = {\n' \
            '[\n' \
            'StringEntry(name + "_0", value1[0]),\n' \
            'IntegerEntry(name + "_1", value2[0]),\n' \
            'BooleanEntry(name + "_2", value3[0]) ]\n' \
            '}\n' \
            '\n' \
            '@Callable(i)\n' \
            'func storeBinaryValue(name: String, value: ByteVector) = {\n' \
            '[BinaryEntry(name, value)]\n' \
            '}\n' \
            '\n' \
            '@Callable(i)\n' \
            'func storeBooleanValue(name: String, value: Boolean) = {\n' \
            '[BooleanEntry(name, value)]\n' \
            '}'

    tx = myAddress.setScript(script, txFee=500000)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']