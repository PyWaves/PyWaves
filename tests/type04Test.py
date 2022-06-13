from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_AssetTransactionWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')

    with pytest.raises(Exception) as error:
        myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), myToken, 3)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_AssetTransactionWithAmountSmallerEqualsZero():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey= '6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')

    with pytest.raises(Exception) as error:
        myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), myToken, -1)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Amount must be > 0\') tblen=3>'

def test_NonExistantAssetTransaction():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('Test')

    with pytest.raises(Exception) as error:
        myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), myToken, 1)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Asset not issued\') tblen=3>'

def test_AssetTransactionButAmountBiggerThanBalance():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')

    with pytest.raises(Exception) as error:
        myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), myToken, 50000)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient asset balance\') tblen=3>'

def test_succesfullAssetTransaction():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey = '6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')

    tx = myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), myToken, 5)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_transactionWithNotAsset():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')

    with pytest.raises(Exception) as error:
        myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'),'', 1000000000)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_transactionFeeIsBiggerThanSelfBalance():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')

    with pytest.raises(Exception) as error:
        myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), myToken, 50, feeAsset = myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient asset balance for fee\') tblen=3>'

def test_successfulTransactionWithSponsoredFee():
    helpers = Helpers()
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')

    tx = myAddress.sendAsset(address.Address('3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ'), myToken, 5, feeAsset = myToken, txFee=1)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']