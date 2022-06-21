from .. import pywaves as pw
from .. import address
from .helpers import Helpers
import pytest

pw.setThrowOnError(True)

def test_assets():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3MsZyHzDhSAVDcd7S1bHo6wgxcxvertc5GJ')
    returnValue = myAddress.assets()

    assert len(returnValue) >= 0