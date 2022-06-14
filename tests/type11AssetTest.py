from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_AssetMassTransferWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 200},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 200}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferAssets(transfers, myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_AssetMassTransferWithTooMuchRecipients():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')

    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100},
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 100},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 100}

    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferAssets(transfers, myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Too many recipients\') tblen=3>'

def test_FeeIsBiggerThanAmountMassTransfer():
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')
    myAddress = address.Address(privateKey='G6aEiT1ih4jwLfgJ89EvULbsziixDuqnEUTpEkvZ76hv')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 200},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 200}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferAssets(transfers, myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_AmountIsBiggerThanBalanceMassTransfer():
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')
    myAddress = address.Address(privateKey='EVXrFCicNRsvhK1CxvDmgkcfVEA16F7g21UQnWAqEWbL')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 270},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 270}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferAssets(transfers, myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\"Insufficient b\'Test\' balance\") tblen=3>'

def test_SuccesfullAssetMassTransfer():
    helpers = Helpers()
    myToken = asset.Asset('fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 10},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 10}
    ]
    tx = myAddress.massTransferAssets(transfers, myToken)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']