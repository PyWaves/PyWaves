from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_sponsoringAssetWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    myToken = asset.Asset('AwzcZy7WwKHAooZJ9GQprQX9igweouMbACWqTmZDXYsU')

    with pytest.raises(Exception) as error:
        myAddress.sponsorAsset(myToken, minimalFeeInAssets= 1000000)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_succesfullSponsoringAsset():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    tx = myAddress.sponsorAsset(assetId='CqjrpvFPNuDWfAqXDAcmdFHGdSzBTZ8Ne6F2VLURQ2sF', minimalFeeInAssets = 1000000)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']