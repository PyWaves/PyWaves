from .. import pywaves as pw
from .. import address
from .. import asset
import pytest

pw.setThrowOnError(True)

def test_updateAssetInfo():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='6QLmHwd62jaGs2A4qS3L6iuuDJCnS343EfafhPRt7nBX')
    myToken = 'fSzvjKJbHXt74GGtoExLtppgXiBXGAf8337exBe4XCE'

    tx = myAddress.updateAssetInfo(myToken, 'jdahdja', 'This is just a test to see a change')

    assert ('error' in tx and 'before' in tx['message']) or ('id' in tx)