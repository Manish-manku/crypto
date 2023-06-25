import random
from nose.tools import assert_raises
from paillierlib import paillier


import sys
     
a = 5
b = 10      

key_pair= paillier.keygen(256)

a2 = paillier.encrypt(a,key_pair.public_key)
b2 = paillier.encrypt(b,key_pair.public_key)

print("A: ",a)
print("B: ",b)
print("Cipher(A): ",a2)
print("Cipher(B): ",b2)

x = paillier.decrypt(a2 + b2, key_pair.private_key) 
y = paillier.decrypt(b2 - a2, key_pair.private_key) 
z = paillier.decrypt(a2 + a2 + b2, key_pair.private_key) 
 
print("x: ",x)
print("y: ",y)
print("decrypt(x): ",x)
print("decrypt(y): ",y)
print("decrypt(z): ",z)


