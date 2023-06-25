import random
import base64
import hashlib

g=3
p=1001
x=random.randint(5, 20)
y=random.randint(10,15)



A=pow(g,x,p)

B=pow(g,y,p)


print ('g: ',g,' (a shared value), n: ',p, ' (a prime number)')

print ('\nAlice calculates:')
print ('a (Alice random): ',x)
print ('Alice value (A): ',A,' (g^a) mod p')


print ('\nBob calculates:')
print ('b (Bob random): ',y)
print ('Bob value (B): ',B,' (g^b) mod p')


print  ('\nAlice calculates:')
keyA=pow(B,x, p)
print ('Key: ',keyA,' (B^a) mod p')
print ('Key: ',hashlib.sha256(keyA.to_bytes(32, byteorder = 'big')).hexdigest())

print ('\nBob calculates:')
keyB=pow(A,y,p)
print ('Key: ',keyB,' (A^b) mod p')
print ('Key: ',hashlib.sha256(keyB.to_bytes(32, byteorder = 'big')).hexdigest())
