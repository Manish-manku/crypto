import random
import h
import sys
     
a = 5
b = 10      

priv, pub = h.generate_keypair(128)

ca, cb = h.encrypt(pub, a), h.encrypt(pub, b)

print("A: ",a)
print("B: ",b)
print("Cipher(A): ",ca)
print("Cipher(B): ",cb)

cs = h.e_add(pub, ca, cb)
s = h.decrypt(priv, pub, cs)
print("Result (Add): ",s)

cs = h.e_add_const(pub, ca, b)
s = h.decrypt(priv, pub, cs)
print("Result (Add): ",s)

cs = h.e_mul_const(pub, ca, b)
s = h.decrypt(priv, pub, cs)
print("Result (Mult): ",s)

p=101
iinv = h.invmod(a, p)
print("(Valx",a,") mod 101 = 1. Val: ",iinv)