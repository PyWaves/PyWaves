from .. import pywaves as pw
from .. import address
import pytest

def test_mainnetAddressCreationBySeed():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    addr = address.Address(seed = 'this is just a dummy test seed')

    assert addr.address.startswith('3P')

def test_mainnetAddressCreationByPublicKey():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    addr = pw.Address(publicKey = 'H8PctYGqhsbbjgmJD5YgyMv6KuNXNAmZt3ho1Jym7Vir')

    assert addr.address.startswith('3PRAjhruvziPqhkeixrejgzdtWrQY1eUTjB')

def test_mainnetAddressCreationByAddress():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    addr = pw.Address(address = '3PRAjhruvziPqhkeixrejgzdtWrQY1eUTjB')

    assert addr.address.startswith('3PRAjhruvziPqhkeixrejgzdtWrQY1eUTjB')

def test_mainnetAddressCreationWithInvalidAddress():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    with pytest.raises(ValueError) as valueError:
        address.Address(address = '3RAjhruvziPqhkeixrejgzdtWrQY1eUTjB')

    assert str(valueError) == '<ExceptionInfo ValueError(\'Invalid address\') tblen=2>'

def test_mainnetAddressCreationWithEmptyPrivateKey():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    with pytest.raises(ValueError) as valueError:
        address.Address()

    assert str(valueError) == '<ExceptionInfo ValueError(\'Empty private key not allowed\') tblen=2>'

def test_testnetAddressCreationBySeed():
    pw.setNode('https://nodes-testnet.wavesnodes.com', 'T')
    addr = address.Address(seed='this is just a dummy test seed')

    assert addr.address.startswith('3N')

def test_stagenetAddressCreationBySeed():
    pw.setNode('https://nodes-stagenet.wavesnodes.com', 'S')
    addr = pw.Address(seed='this is just a dummy test seed')

    assert addr.address.startswith('3M')

def test_mainnetWithAlias():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    addr = pw.Address(alias = 'hawky')

    assert addr.address.startswith('3P')

def test_mainnetWithPrivateKey():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    addr = pw.Address(privateKey = 'DQP9aFogWUJKGthnyERXU8jfVfp9CimCkGXVaMyyFyLM')

    assert addr.address.startswith('3P')

def test_mainnetWithNonce():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    addr = pw.Address(seed = 'this is just a dummy test seed', nonce = 1)

    assert addr.address.startswith('3P')

def test_mainnetWithNegativeNonce():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    with pytest.raises(ValueError) as valueError:
        addr = pw.Address(seed='this is just a dummy test seed', nonce=-5)

    assert str(valueError) == '<ExceptionInfo ValueError(\'Nonce must be between 0 and 4294967295\') tblen=2>'

def test_mainnetWithHugeNonce():
    pw.setNode('https://nodes.wavesnodes.com', 'W')
    with pytest.raises(ValueError) as valueError:
        addr = pw.Address(seed='this is just a dummy test seed', nonce=4294967297)

    assert str(valueError) == '<ExceptionInfo ValueError(\'Nonce must be between 0 and 4294967295\') tblen=2>'