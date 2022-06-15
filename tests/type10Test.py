from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import random
import string
import pytest

pw.setThrowOnError(True)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

def test_aliasWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    with pytest.raises(Exception) as error:
        myAddress.createAlias('TestAlias')

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_succesfullAlias():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    randomString = get_random_string(8)

    tx = myAddress.createAlias(randomString)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']
