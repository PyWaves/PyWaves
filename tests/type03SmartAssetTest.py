from .. import pywaves as pw
from .. import address
from .helpers import Helpers
import pytest

pw.setThrowOnError(True)

def test_issueSmartAssetWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')

    script = 'match tx { \n' + \
             '  case _ => true\n' + \
             '}'

    with pytest.raises(Exception) as error:
        myAddress.issueSmartAsset('SmartAsset2', 'This is just a test smart asset', 10000000, scriptSource = script)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_nameTooShort():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    script = 'match tx { \n' + \
             '  case _ => true\n' + \
             '}'

    with pytest.raises(Exception) as error:
        myAddress.issueSmartAsset('Sma', 'This is just a test smart asset', 10000000, scriptSource=script)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Asset name must be between 4 and 16 characters long\') tblen=3>'

def test_nameTooLong():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    script = 'match tx { \n' + \
             '  case _ => true\n' + \
             '}'

    with pytest.raises(Exception) as error:
        myAddress.issueSmartAsset('SmartTestAssetTeststst', 'This is just a test smart asset', 10000000, scriptSource=script)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Asset name must be between 4 and 16 characters long\') tblen=3>'


def test_pywavesOffline():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    script = 'match tx { \n' + \
             'case _ => true\n' + \
             '}'

    pw.setOffline()
    with pytest.raises(Exception) as error:
        myAddress.issueSmartAsset('SMartAsset', 'This is just a test smart asset', 10000000, scriptSource = script)

    assert str(error) == '<ExceptionInfo PyWavesException(\'PyWaves currently offline\') tblen=3>'
    pw.setOnline()

def test_succesfullIssueSmartAsset():
    pw.setOnline()
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

    script = 'match tx { \n' + \
             'case _ => true\n' + \
             '}'

    tx = myAddress.issueSmartAsset('SMartAsset', 'This is just a test smart asset', 10000000, scriptSource = script)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']