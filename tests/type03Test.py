from .helpers import Helpers
from .. import pywaves as pw
from .. import address
import pytest

pw.setThrowOnError(True)

def test_issueAssetWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAdress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    with pytest.raises(Exception) as error:
       myAdress.issueAsset('Test2','This is just another test asset', 100000, 1)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_issueAssetWithTooShortName():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAdress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    with pytest.raises(Exception) as error:
       myAdress.issueAsset('Tes','This is just another test asset', 100000, 1)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Asset name must be between 4 and 16 characters long\') tblen=3>'

def test_pywavesOffline():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAdress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    pw.setOffline()
    tx = myAdress.issueAsset('Test2', 'this is just another test asset',10000,0)
    pw.setOnline()

    assert tx['api-type'] == 'POST'

def test_issueAssetWithTooLongName():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAdress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    with pytest.raises(Exception) as error:
       myAdress.issueAsset('12345678912345678','This is just another test asset', 100000, 1)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Asset name must be between 4 and 16 characters long\') tblen=3>'

def test_succesfullIssueAsset():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAdress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    asset = myAdress.issueAsset('Test', 'This is just a test token', 1000000, 0)
    id = asset.assetId
    blockchainTx = helpers.waitFor(id)

    assert blockchainTx['id'] == id