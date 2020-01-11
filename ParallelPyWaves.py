# Copyright (C) 2017 PyWaves Developers
#
# This file is part of PyWaves.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals
import logging

from .address import *
from .asset import *
from .order import *
from .contract import *
from .oracle import *
from .ParallelPyWaves import *

class ParallelPyWaves(object):
    def __init__(self):
        self.DEFAULT_TX_FEE = 100000
        self.DEFAULT_BASE_FEE = self.DEFAULT_TX_FEE
        self.DEFAULT_SMART_FEE = 400000
        self.DEFAULT_ASSET_FEE = 100000000
        self.DEFAULT_MATCHER_FEE = 300000
        self.DEFAULT_LEASE_FEE = 100000
        self.DEFAULT_ALIAS_FEE = 100000
        self.DEFAULT_SPONSOR_FEE = 100000000
        self.DEFAULT_SCRIPT_FEE = 100000
        self.DEFAULT_ASSET_SCRIPT_FEE = 100000000
        self.DEFAULT_SET_SCRIPT_FEE = 1000000
        self.DEFAULT_INVOKE_SCRIPT_FEE = 500000
        self.DEFAULT_CURRENCY = 'WAVES'
        self.VALID_TIMEFRAMES = (5, 15, 30, 60, 240, 1440)
        self.MAX_WDF_REQUEST = 100

        self.THROW_EXCEPTION_ON_ERROR = False

        self.OFFLINE = False
        self.NODE = 'https://nodes.wavesnodes.com'

        self.ADDRESS_VERSION = 1
        self.ADDRESS_CHECKSUM_LENGTH = 4
        self.ADDRESS_HASH_LENGTH = 20
        self.ADDRESS_LENGTH = 1 + 1 + self.ADDRESS_CHECKSUM_LENGTH + self.ADDRESS_HASH_LENGTH

        self.CHAIN = 'mainnet'
        self.CHAIN_ID = 'W'
        self.MATCHER = 'https://matcher.waves.exchange'
        self.MATCHER_PUBLICKEY = ''

        self.DATAFEED = 'http://marketdata.wavesplatform.com'

        logging.getLogger("requests").setLevel(logging.WARNING)
        console = logging.StreamHandler()
        console.setLevel(logging.ERROR)
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

        self.WAVES = Asset('')
        self.BTC = Asset('8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS')
        self.USD = Asset('Ft8X1v1LTa1ABafufpaCWyVj8KkaxUWE6xBhW6sNFJck')

    def throw_error(self, msg):
        if self.THROW_EXCEPTION_ON_ERROR:
            raise PyWavesException(msg)

    def setThrowOnError(self, throw=True):
        self.THROW_EXCEPTION_ON_ERROR = throw


    def setOffline(self):
        self.OFFLINE = True

    def setOnline(self):
        self.OFFLINE = False

    def setChain(self, chain = '', chain_id = None):
        if chain == '':
            chain = self.CHAIN

        if chain_id is not None:
            self.CHAIN = chain
            self.CHAIN_ID = chain_id
        else:
            if chain.lower()=='mainnet' or chain.lower()=='w':
                self.CHAIN = 'mainnet'
                self.CHAIN_ID = 'W'
            elif chain.lower()=='hacknet' or chain.lower()=='u':
                self.CHAIN = 'hacknet'
                self.CHAIN_ID = 'U'
            else:
                self.CHAIN = 'testnet'
                self.CHAIN_ID = 'T'

    def getChain(self):
        return self.CHAIN

    def setNode(self, node = '', chain = '', chain_id = None):
        if node == '':
            node = self.NODE

        if chain == '':
            chain = self.CHAIN

        self.NODE = node
        self.setChain(chain, chain_id)

    def getNode(self):
        return self.NODE

    def setMatcher(self, node = ''):
        if node == '':
            node = self.MATCHER

        try:
            self.MATCHER_PUBLICKEY = self.wrapper('/matcher', host = node)
            self.MATCHER = node
            logging.info('Setting matcher %s %s' % (self.MATCHER, self.MATCHER_PUBLICKEY))
        except:
            self.MATCHER_PUBLICKEY = ''

    def setDatafeed(self, wdf = ''):
        if wdf == '':
            wdf = self.DATAFEED

        self.DATAFEED = wdf
        logging.info('Setting datafeed %s ' % (self.DATAFEED))

    def wrapper(self, api, postData='', host='', headers=''):
        #global OFFLINE
        if self.OFFLINE:
            offlineTx = {}
            offlineTx['api-type'] = 'POST' if postData else 'GET'
            offlineTx['api-endpoint'] = api
            offlineTx['api-data'] = postData
            return offlineTx
        if not host:
            host = self.NODE
        if postData:
            req = requests.post('%s%s' % (host, api), data=postData, headers={'content-type': 'application/json'}).json()
        else:
            req = requests.get('%s%s' % (host, api), headers=headers).json()
        return req

    def height(self):
        return self.wrapper('/blocks/height')['height']

    def lastblock(self):
        return self.wrapper('/blocks/last')

    def block(self, n):
        return self.wrapper('/blocks/at/%d' % n)

    def tx(self, id):
        return self.wrapper('/transactions/info/%s' % id)

    def getOrderBook(self, assetPair):
        orderBook = assetPair.orderbook()
        try:
            bids = orderBook['bids']
            asks = orderBook['asks']
        except:
            bids = ''
            asks = ''
        return bids, asks

    def symbols(self):
        return self.wrapper('/api/symbols', host=self.DATAFEED)

    def markets(self):
        return self.wrapper('/api/markets', host=self.DATAFEED)

    def validateAddress(self, address):
        addr = crypto.bytes2str(base58.b58decode(address))
        if addr[0] != chr(self.ADDRESS_VERSION):
            logging.error("Wrong address version")
        elif addr[1] != self.CHAIN_ID:
            logging.error("Wrong chain id")
        elif len(addr) != self.ADDRESS_LENGTH:
            logging.error("Wrong address length")
        elif addr[-self.ADDRESS_CHECKSUM_LENGTH:] != crypto.hashChain(crypto.str2bytes(addr[:-self.ADDRESS_CHECKSUM_LENGTH]))[:self.ADDRESS_CHECKSUM_LENGTH]:
            logging.error("Wrong address checksum")
        else:
            return True
        return False

class PyWavesException(ValueError):
    pass