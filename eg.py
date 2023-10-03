# Python program to illustrate ElGamal encryption
import random
from math import pow
import timeit
a = random.randint(2, 10)

def gcd(a, b):
	if a < b:
		return gcd(b, a)
	elif a % b == 0:
		return b;
	else:
		return gcd(b, a % b)

# Generating large random numbers
def gen_key(q):
	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)
	return key

# Modular exponentiation
def power(a, b, c):#a^b%c
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c;
		y = (y * y) % c
		b = int(b / 2)

	return x % c

# Asymmetric encryption
def encrypt(msg, q, h, g):

	en_msg = []

	k = gen_key(q)#Private key for sender
	s = power(h, k, q)
	p = power(g, k, q)
	
	for i in range(0, len(msg)):
		en_msg.append(msg[i])
	#print("g^k used : ", p)
	#print("cipher text : ", s)
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])
	for i in range(0, len(en_msg)):
		print(en_msg[i]) 
	return en_msg, p

def decrypt(en_msg, p, key, q):

	dr_msg = []
	h = power(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))
	return dr_msg

# Driver code
def main():

	msg = input("enter the message:")
	print("Original Message :", msg)
	q = random.randint(pow(10, 20), pow(10, 50))
	g = random.randint(2, q)
	kgs = timeit.default_timer()
	key = gen_key(q)# Private key for receive
	#print("key generation:",(%.2f)(timeit.default_timer() - kgs)*1000000))
	hh=(timeit.default_timer() - kgs)*1000000
	print("key generation time %.2f"%hh)
	h = power(g, key, q)
	#print("generated key : ", g)
	#print("g^a used : ", h)
	es=timeit.default_timer()
	en_msg, p = encrypt(msg, q, h, g)
	#print("encryption time:",(timeit.default_timer()-es)*1000000)
	et=(timeit.default_timer()-es)*1000000
	print("key generation time %.2f"%et)
	ds=timeit.default_timer()
	dr_msg = decrypt(en_msg, p, key, q)
	#print("decryption time:",(timeit.default_timer()-ds)*1000000)
	dt=(timeit.default_timer()-es)*1000000
	print("key generation time %.2f"%dt)
	dmsg = ''.join(dr_msg)
	print("Decrypted Message :", dmsg)
	print("total time",(timeit.default_timer() - kgs)*1000000)
#for i in range(50):
if __name__ == '__main__':
	main()