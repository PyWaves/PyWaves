from .helpers import Helpers
from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_assetMassTransferWithoutPrivateKey():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setOnline()
    myAddress = address.Address('3MwGH6GPcq7jiGNXgS4K6buynpLZR5LAgQm')
    myToken = asset.Asset('7oSYZxQUvB8aKqPQupqQt2b5nipegxkR1vszFQVH6Gjg')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 200},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 200}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferAssets(transfers, myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Private key required\') tblen=3>'

def test_assetMassTransferWithTooMuchRecipients():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setOnline()
    myToken = asset.Asset('7oSYZxQUvB8aKqPQupqQt2b5nipegxkR1vszFQVH6Gjg')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')

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

def test_feeIsBiggerThanAmountMassTransfer():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setOnline()
    myToken = asset.Asset('7oSYZxQUvB8aKqPQupqQt2b5nipegxkR1vszFQVH6Gjg')
    myAddress = address.Address(privateKey='G6aEiT1ih4jwLfgJ89EvULbsziixDuqnEUTpEkvZ76hv')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 200},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 200}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferAssets(transfers, myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\'Insufficient Waves balance\') tblen=3>'

def test_amountIsBiggerThanBalanceMassTransfer():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setOnline()
    myToken = asset.Asset('JE8G7MGsGAmwMRbnBG9GrdTdHqQ8SFtrJ8As8GjkPoh3')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 5000000},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 500000000}
    ]

    with pytest.raises(Exception) as error:
        myAddress.massTransferAssets(transfers, myToken)

    assert str(error) == '<ExceptionInfo PyWavesException(\"Insufficient b\'Test\' balance\") tblen=3>'

def test_succesfullAssetMassTransfer():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setOnline()
    helpers = Helpers()
    myToken = asset.Asset('7oSYZxQUvB8aKqPQupqQt2b5nipegxkR1vszFQVH6Gjg')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 10},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 10}
    ]
    tx = myAddress.massTransferAssets(transfers, myToken)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_succesfullSmartAssetMassTransfer():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setOnline()
    helpers = Helpers()
    myToken = asset.Asset('APPVkPEmQE6h7xj2dwKJfrSyxKku4r9GVFwFT5TxJYTb')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 10},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 10}
    ]
    tx = myAddress.massTransferAssets(transfers, myToken)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']

def test_massTransferAssetsFromAccountThatExceedComplexityThreshold():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    pw.setOnline()
    helpers = Helpers()
    myToken = asset.Asset('64CxbqQLW67PyJjEdNKNTP566MqArvPmtRXWZUTFwsv7')
    myAddress = address.Address(privateKey='1sbUjTHo19h8NghyMQJBnwKfeErykku6STdJW8XevhJ')
    transfers = [
        {'recipient': '3MuqNWyf4RMWz3cqDi4QZRVr9v76LKMjNVZ', 'amount': 1},
        {'recipient': '3MxM7eBUqScwAdnqPzrUmiZEewhkvSqqVJY', 'amount': 1}
    ]
    tx = myAddress.massTransferAssets(transfers, myToken)
    blockchainTx = helpers.waitFor(tx['id'])

    assert blockchainTx['id'] == tx['id']