#!/usr/bin/env python3

import address

# Generate a new empty address and print it
myAddress = address.Address()
print(myAddress)

# Copy over the values
myaddress = myAddress.address
mypublicKey = myAddress.publicKey
myprivateKey = myAddress.privateKey
myseed = myAddress.seed

# Use the values to create the Address object for each of the initialization variables.
del(myAddress)
myAddress = address.Address(address=myaddress)
print(myAddress)
del(myAddress)
myAddress = address.Address(seed=myseed)
print(myAddress)
del(myAddress)
myAddress = address.Address(publicKey=mypublicKey)
print(myAddress)
del(myAddress)
myAddress = address.Address(privateKey=myprivateKey)
print(myAddress)

# For now visually check the output te be sane.