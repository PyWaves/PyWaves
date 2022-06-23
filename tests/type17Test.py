from .. import pywaves as pw
from .. import address

pw.setThrowOnError(True)

def test_updateAssetInfo():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='BGpBRDeUiHskf4bdyWoUAKpP9DSx51haovHcGNqPEy6Q')
    myToken = '7oSYZxQUvB8aKqPQupqQt2b5nipegxkR1vszFQVH6Gjg'

    tx = myAddress.updateAssetInfo(myToken, 'jdahdja', 'This is just a test to see a change')

    assert ('error' in tx and 'before' in tx['message']) or ('id' in tx)