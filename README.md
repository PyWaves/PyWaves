# PyWaves
PyWaves is an object-oriented Python interface to the Waves blockchain platform.

## Getting Started

You can install PyWaves using:

    pip install pywaves

## Documentaion

The library utilizes classes to represent various Waves data structures:

* pywaves.Address
* pywaves.Asset
* pywaves.AssetPair
* pywaves.Order

####Code Example
```python
import pywaves as pw

myAddress = pw.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')
otherAddress = pw.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM')
myAddress.sendWaves(otherAddress, 10000000)
myToken = myAddress.issueAsset('Token1', 'My Token', 1000, 0)
while not myToken.status():
	pass
myAddress.sendAsset(otherAddress, myToken, 50)

```

###Address Class
__pywaves.Address(address, publicKey, privateKey, seed)__ _Creates a new Address object_

####attributes:
- _address_
- _publicKey_
- _privateKey_
- _seed_

####methods:

`balance(assetId='', confirmations=0)` returns balance of Waves or other assets

`assets()` returns a list of assets owned by the address

`issueAsset(name, description, quantity, decimals=0, reissuable=False, txFee=DEFAULT_ASSET_FEE)` issue a new asset

`reissueAsset(Asset, quantity, reissuable=False, txFee=DEFAULT_ASSET_FEE)` reissue an asset

`burnAsset(Asset, quantity, txFee=DEFAULT_ASSET_FEE)` burn the specified quantity of an asset

`sendWaves(recipient, amount, attachment='', txFee=DEFAULT_TX_FEE)` send specified amount of Waves to recipient

`sendAsset(recipient, asset, amount, attachment='', txFee=DEFAULT_TX_FEE)` send specified amount of an asset to recipient

`cancelOrder(assetPair, order)` cancel an order

`buy(assetPair, amount, price, maxLifetime=30*86400, matcherFee=DEFAULT_MATCHER_FEE)` post a buy order

`sell(assetPair, amount, price, maxLifetime=30*86400, matcherFee=DEFAULT_MATCHER_FEE)` post a sell order

`lease(recipient, amount, txFee=DEFAULT_LEASE_FEE)` post a lease transaction

`leaseCancel(leaseId, txFee=DEFAULT_LEASE_FEE)` cancel a lease 

###Asset Class
__pywaves.Asset(assetId)__ _Creates a new Asset object_

####attributes:
- _status_
- _assetId_	
- _issuer_
- _name_
- _description_	
- _quantity_
- _decimals_ = 0
- _reissuable = False_

####methods:
`status()` returns 'Issued' if the asset exists


###AssetPair Class
__pywaves.AssetPair(asset1, asset2)__ _Creates a new AssetPair object with 2 Asset objects_

####attributes:
- _asset1_
- _asset2_

###Order Class
__pywaves.Order(orderId, assetPair, address='')__ Creates a new Order object

####attributes:
- _status_
- _orderId_
- _assetPair_
- _address_
- _matcher_
- _matcherPublicKey_

####methods:
`status()` returns current order status
`cancel()` cancel the order


##Other functions
`pywaves.setNode(node, chain)`  sets node URL ('http://ip-address:port') and chain (either 'mainnet' or 'testnet')

`pywaves.setMatcher(node)`  set matcher URL ('http://ip-address:port')

`pywaves.height()` returns blockchain height

`pywaves.lastblock()` returns last block

`pywaves.block(n)` returns block at specified height

`pywaves.tx(id)` returns transaction details



### Default Fees
The fees for waves/asset transfers, asset issue/reissue/burn and matcher transactions are set by default as follows:
* DEFAULT_TX_FEE = 100000
* DEFAULT_ASSET_FEE = 100000000
* DEFAULT_MATCHER_FEE = 1000000
* DEFAULT_LEASE_FEE = 100000


## More Examples

####Playing with addresses:

```python
import pywaves as pw

# generate a new address
myAddress = pw.Address()  

# set an address with a public key
myAddress = pw.Address('3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh')

# get an existing address from seed
myAddress = pw.Address(seed='seven wrist bargain hope pattern banner plastic maple student chaos grit next space visa answer')

# get an existing address from privateKey
myAddress = pw.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')
```

####Balances:
```python
import pywaves as pw

myAddress = pw.Address('3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh')

# get Waves balance
print("Your balance is %18d" % myAddress.balance())

# get Waves balance after 20 confirmations 
print("Your balance is %18d" % myAddress.balance(confirmations = 20))

# get an asset balance
print("Your asset balance is %18d" % myAddress.balance('DHgwrRvVyqJsepd32YbBqUeDH4GJ1N984X8QoekjgH8J'))
```

####Waves and asset transfers:
```python
import pywaves as pw

myAddress = pw.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')

# send Waves to another address
myAddress.sendWaves(recipient = pw.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM'),
					amount = 100000000)

# send asset to another address
myToken = pw.Asset('4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV')
myAddress.sendAsset(recipient = pw.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM'),
					asset = myToken,
					amount = 1000)
```

####Issuing an asset:
```python
import pywaves as pw

myToken = myAddress.issueToken(name = "MyToken",
					 		   description = "This is my first token",
					 		   quantity = 1000000,
					 		   decimals = 2)
```

####Mass payment:
```python
import pywaves as pw

recipients = ['3PBbp6bg2YEnHfdJtYM7jzzXYQeb7sx5oFg',
			  '3P4A27aCd3skNja46pcgrLYEnK36TkSzgUp',
			  '3P81U3ujotNUwZMWALdcJQLzBVbrAuUQMfs',
			  '3PGcKEMwQcEbmeL8Jhe9nZQRBNCNdcHCoZP',
			  '3PKjtzZ4FhKrJUikbQ1hRk5xbwVKDyTyvkn']

myAddress = pw.Address(privateKey = "CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S")

for address in recipients:
	myAddress.sendWaves(pw.Address(address), 1000000)
```

####Token airdrop:
```python
import pywaves as pw

myAddress = pw.Address(privateKey = 'CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')
myToken = pw.Asset('4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV')
amount = 1000

with open('recipients.txt') as f:
	lines = f.readlines()
for address in lines:
	myAddress.sendAsset(pw.Address(address.strip()), myToken, amount)
```

####Playing with Waves Matcher node (DEX):
```python	
import pywaves as pw

# set Matcher node to use
pw.setMatcher(node = 'http://127.0.0.1:6886')

# post a buy order
BTC = pw.Asset('4ZzED8WJXsvuo2MEm2BmZ87Azw8Sx7TVC6ufSUA5LyTV')
USD = pw.Asset('6wuo2hTaDyPQVceETj1fc5p4WoMVCGMYNASN8ym4BGiL')
BTC_USD = pw.AssetPair(BTC, USD)
myOrder = myAddress.buy(assetPair = BTC_USD, amount = 15, price = 950.75)

# post a sell order
WCT = pw.Asset('6wuo2hTaDyPQVceETj1fc5p4WoMVCGMYNASN8ym4BGiL')
Incent = pw.Asset('FLbGXzrpqkvucZqsHDcNxePTkh2ChmEi4GdBfDRRJVof')
WCT_Incent = pw.AssetPair(WCT, Incent)
myOrder = myAddress.sell(assetPair = WCT_Incent, amount = 100, price = 2.50)

# cancel an order
myOrder.cancel()
# or
myAddress.cancelOrder(assetPair, myOrder)

```

####LPOS
```python
import pywaves as pw

# connect to a local testnet node
pw.setNode(node = 'http://127.0.0.1:6869', chain = 'testnet')

myAddress = pw.Address(privateKey = 'CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')
minerAddress = pw.Address('3PBbp6bg2YEnHfdJtYM7jzzXYQeb7sx5oFg')

# lease 1000 Waves to minerAddress
leaseId = myAddress.lease(minerAddress, 100000000000)

# revoke the lease
myAddress.leaseCancel(leaseId)

```


### Using PyWaves in a Python shell

#### Check an address balance:
```
>>> import pywaves as pw
>>> pw.Address('3P31zvGdh6ai6JK6zZ18TjYzJsa1B83YPoj')
address = 3P31zvGdh6ai6JK6zZ18TjYzJsa1B83YPoj
publicKey = 
privateKey = 
seed = 
balances:
  Waves = 1186077288304570
  BDMRyZsmDZpgKhdM7fUTknKcUbVVkDpMcqEj31PUzjMy (Tokes) = 43570656915
  RRBqh2XxcwAdLYEdSickM589Vb4RCemBCPH5mJaWhU9 (Ripto Bux) = 4938300000000
  4rmhfoscYcjz1imNDvtz45doouvrQqDpbX7xdfLB4guF (incentCoffee) = 7
  Ftim86CXM6hANxArJXZs2Fq7XLs3nJvgBzzEwQWwQn6N (Waves) = 2117290600000000
  E4ip4jzTc4PCvebYn1818T4LNoYBVL3Y4Y4dMPatGwa9 (BitCoin) = 500000000000
  FLbGXzrpqkvucZqsHDcNxePTkh2ChmEi4GdBfDRRJVof (Incent) = 12302659925430
  GQr2fpkfmWjMaZCbqMxefbiwgvpcNgYdev7xpuX6xqcE (KISS) = 1000
  DxG3PLganyNzajHGzvWLjc4P3T2CpkBGxY4J9eJAAUPw (UltraCoin) = 200000000000000
  4eWBPyY4XNPsFLoQK3iuVUfamqKLDu5o6zQCYyp9d8Ae (LIKE) = 1000
>>> 
```

#### Generate a new address:
```
>>> import pywaves as pw
>>> pw.Address()
address = 3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh
publicKey = EYNuSmW4Adtcc6AMCZyxkiHMPmF2BZ2XxvjpBip3UFZL
privateKey = CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S
seed = seven wrist bargain hope pattern banner plastic maple student chaos grit next space visa answer
balances:
  Waves = 0
>>> 
```

#### Check an asset:
```
>>> import pywaves as pw
>>> pw.Asset('DHgwrRvVyqJsepd32YbBqUeDH4GJ1N984X8QoekjgH8J')
status = Issued
assetId = DHgwrRvVyqJsepd32YbBqUeDH4GJ1N984X8QoekjgH8J
issuer = 3PPKF2pH4KMYgsDixjrhnWrPycVHr1Ye37V
name = WavesCommunity
description = Waves community token.
quantity = 1000000000
decimals = 2
reissuable = False
```

#### Post an order and check its status:
```
>>> myOrder = myAddress.buy(pw.AssetPair(token1, token2), 1, 25)
>>> myOrder
status = Accepted
id = ARZdYgfXz3ksRMvhnGeLLJnn3CQnz7RCa7U6dVw3zert
asset1 = AFzL992FQbhcgSZGKDKAiRWcjtthM55yVCE99hwbHf88
asset2 = 49Aha2RR2eunR3KZFwedfdi7K9v5MLQbLYcmVdp2QkZT
sender.address = 3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh
sender.publicKey = EYNuSmW4Adtcc6AMCZyxkiHMPmF2BZ2XxvjpBip3UFZL
matcher = http://127.0.0.1:6886
```

#### Cancel the order
```
>>> myOrder.cancel()
>>> myOrder
status = Cancelled
id = ARZdYgfXz3ksRMvhnGeLLJnn3CQnz7RCa7U6dVw3zert
asset1 = AFzL992FQbhcgSZGKDKAiRWcjtthM55yVCE99hwbHf88
asset2 = 49Aha2RR2eunR3KZFwedfdi7K9v5MLQbLYcmVdp2QkZT
sender.address = 3P6WfA4qYtkgwVAsWiiB6yaea2X8zyXncJh
sender.publicKey = EYNuSmW4Adtcc6AMCZyxkiHMPmF2BZ2XxvjpBip3UFZL
matcher = http://127.0.0.1:6886
```


## Connecting to a different node or chain

PyWaves supports both mainnet and testnet chains. By default, PyWaves connects to the mainnet RPC server at https://nodes.wavesnodes.com. It's possible to specify a different server and chain with the setNode() function

```python
import pywaves as pw

# connects to a local testnet node
pw.setNode(node = 'http://127.0.0.1:6869', chain = 'testnet')

# connects to a local mainnet node
pw.setNode(node = 'http://127.0.0.1:6869', chain = 'mainnet')

```


## License
Code released under the [MIT License](https://github.com/PyWaves/PyWaves/blob/master/LICENSE).

