from .. import pywaves as pw
from .. import address
from .. import asset
from .. import order
from .helpers import Helpers
import pytest
import time

pw.setThrowOnError(True)

def test_setScriptWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    myToken = asset.Asset('5Cs2APZPHeXqhB2At2qWT2wUuCe9SjxitFYdXhj6Q8FL')

    script = 'match tx { \n' + \
             '  case _ => true\n' + \
             '}'

    with pytest.raises(Exception) as error:
        myAddress.setAssetScript(myToken, script)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_assetScriptOnAnAssetWithoutScript():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    myToken = asset.Asset('5Cs2APZPHeXqhB2At2qWT2wUuCe9SjxitFYdXhj6Q8FL')

    script = 'match tx { \n' + \
             '  case _ => true\n' + \
             '}'

    tx = myAddress.setAssetScript(myToken, script)

    assert tx['message'] == 'State check failed. Reason: Cannot set script on an asset issued without a script'


def test_acceptedAssetScript():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    myToken = asset.Asset('2X2xWhF9hzdQa2so459dbnQTBbyikdXqX3cfXiaATufv')

    script = 'match tx { \n' + \
             '  case _ => true\n' + \
             '}'

    tx = myAddress.setAssetScript(myToken, script)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']