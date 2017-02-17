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

import requests

from .address import *
from .asset import *

NODE = 'https://nodes.wavesnodes.com'
CHAIN = 'mainnet'
CHAIN_ID = 'W'
PYWAVES_DIR = os.path.expanduser("~") + "/.pywaves"

MATCHER_HOST = 'dev.pywaves.org'
MATCHER_PORT = 6886
MATCHER_PUBLIC_KEY = 'Bz3T6C1TM1dT5cejqsHVFhw1xnNw3v6u9MT62wYQ2Lwa'
MATCHER_FEE = 100000

if not os.path.exists(PYWAVES_DIR):
    os.makedirs(PYWAVES_DIR)

logging.basicConfig(filename=('%s/pywaves.log' % PYWAVES_DIR),
                        format='%(asctime)-15s [%(levelname)s] %(message)s',
                        level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def setNode(node, chain='mainnet'):
    global NODE, CHAIN, CHAIN_ID, DIR
    NODE = node
    if chain.lower()=='mainnet' or chain.lower()=='w':
        CHAIN = 'mainnet'
        CHAIN_ID = 'W'
    else:
        CHAIN = 'testnet'
        CHAIN_ID = 'T'
    logging.info('Connecting to %s node %s' % (CHAIN, NODE))

def setMatcher(host, port, publicKey, fee):
    global MATCHER_HOST, MATCHER_PORT, MATCHER_PUBLIC_KEY, MATCHER_FEE
    MATCHER_HOST = host
    MATCHER_PORT = port
    MATCHER_PUBLIC_KEY = publicKey
    MATCHER_FEE = fee
    logging.info('Setting matcher %s:%d %s' % (MATCHER_HOST, MATCHER_PORT, MATCHER_PUBLIC_KEY))

def wrapper(api, postData='', host=''):
    if not host:
        host = NODE
    if postData:
        req = requests.post('%s%s' % (host, api), data=postData).json()
    else:
        req = requests.get('%s%s' % (host, api)).json()
    return req

def height():
    return wrapper('/blocks/height')['height']

def lastblock():
    return wrapper('/blocks/last')

def block(n):
    return wrapper('/blocks/at/%d' % n)

def tx(id):
    return wrapper('/transactions/info/%s' % id)

def getOrderBook(assetPair):
    req = wrapper('/matcher/orderBook?asset1=%s&asset2=%s' % (assetPair.asset1, assetPair.asset2), '', host = 'http://%s:%s' % (pywaves.MATCHER_HOST, pywaves.MATCHER_PORT))
    try:
        bids = req['bids']
        asks = req['asks']
    except:
        bids = ''
        asks = ''
    return bids, asks
