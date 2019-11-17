import random
import string
import time

import pywaves as py
import unittest

py.setNode('https://testnode1.wavesnodes.com', 'testnet')

address = py.Address(
    seed='verify upgrade lumber legal pig eternal boy cupboard please action material pyramid')
address2 = py.Address(
    seed="recall whip number deliver immune general pool capable level bulk height deputy shine sudden skull")
BTC=""



class WavesTest(unittest.TestCase):

    # def gen_random_str(self, stringLength=30):
    #     """Generate a random string of fixed length """
    #     letters = string.ascii_lowercase
    #     return ''.join(random.choice(letters) for i in range(stringLength))
    #
    # # Transfer tests
    # def test_tx_fail(self):
    #     output = address.sendWaves(address, 1)
    #     self.assertIn("error", str(output))
    #
    # def test_tx_right(self):
    #     output = address.sendWaves(address, 1, txFee=2000000)
    #     self.assertIn("id", str(output))
    #
    # def test_tx_just_not_enough(self):
    #     output = address.sendWaves(address, 1, txFee=1999999)
    #     self.assertIn("error", str(output))
    #
    # def test_create_alias_error_not_enough_fee(self):
    #     output = address2.createAlias("not_enough_fee", txFee=1000000000)
    #     print(output)
    #     self.assertIn("error", str(output))
    #
    # def test_create_alias_to_long(self):
    #     output = address.createAlias(self.gen_random_str(40), txFee=1000000000)
    #     self.assertIn("length should be between 4 and 30", str(output))
    #
    # def test_alias(self):
    #     output = address.createAlias(self.gen_random_str(40), txFee=1000000000)
    #     self.assertIn("id", str(output))

    def test_lease_enough_fee_and_cancel(self):
        output = address.lease(address2, 1, txFee=2000000)
        self.assertNotIn("error", str(output))
        time.sleep(60)
        output = address.leaseCancel(str(output['id']))
        self.assertNotIn("error", str(output))


if __name__ == '__main__':
    unittest.main()
