from paillierlib import paillier
from gmpy2 import mpz

key_pair = paillier.keygen(128)  

m1 = mpz(10)
m2 = mpz(1)
c1 = paillier.encrypt(m1, key_pair.public_key)
c2 = paillier.encrypt(m2, key_pair.public_key)


paillier.decrypt(c1 + c2, key_pair.private_key) 
paillier.decrypt(c1 - c2, key_pair.private_key) 
paillier.decrypt(c1 + c1 + c2, key_pair.private_key) 

m3 = mpz(2)
d = paillier.decrypt(c1 * m3, key_pair.private_key)

print (c1)
print (c2)
print (d)
