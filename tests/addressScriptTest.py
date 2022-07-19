from .. import pywaves as pw
from .. import address

pw.setThrowOnError(True)

def test_adddressWithScriptThatExceedsComplexityThreshold():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address(privateKey='1sbUjTHo19h8NghyMQJBnwKfeErykku6STdJW8XevhJ')

    result = myAddress.script()

    assert (result['script'].startswith('base64:') and result['extraFee'] == 400000)

def test_addressWithThatDontExceedComplexityThreshold():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')

    myAddress = address.Address(privateKey='HCDG9cDm3zy2o1B6yhb8eYbuPxzW62JSGnu4oRREtPii')

    result = myAddress.script()

    assert (result['script'].startswith('base64:') and result['extraFee'] == 0)

def test_addressWithoutScript():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    myAddress = address.Address('3N13zmzeh3g2cHgWSfvBq6o1CmfZ2UNMuVa')

    result = myAddress.script()

    assert (result['script'] is None and result['extraFee'] == 0)
