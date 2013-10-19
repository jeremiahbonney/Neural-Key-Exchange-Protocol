import copy
import random
from NKEP import *
from TPM import *



def binary_concat(num1, num2):
	concat_num = num1 <<(len(bin(num1))-2) 
	return concat_num + num2

def xor_strings(str1, str2):
	return ''.join([ chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2) ])

def weight_to_string(TPM, amount = 0):
	if amount == 0:
		return ''.join([chr(TPM.weights[x]%95+32) for x in range(TPM.input_num)])
	else:
		return ''.join([chr(TPM.weights[x]%95+32) for x in range(amount)])


def encrypt(TPM, TPM_other, plaintext):
	message_length = len(plaintext)
	key = ""
	while message_length > TPM.input_num:
		key += weight_to_string(TPM)
		message_length-=TPM.input_num
		key_exchange_one_only(TPM, TPM_other)
	key += weight_to_string(TPM, message_length)
	key_exchange_one_only(TPM, TPM_other)
	return xor_strings(plaintext, key)

def decrypt(TPM, TPM_other, ciphertext):
	length_remaining = len(ciphertext)
	key = ""
	while length_remaining > TPM.input_num:
		key += weight_to_string(TPM)
		length_remaining -= TPM.input_num
		key_exchange_one_only(TPM, TPM_other)
	key += weight_to_string(TPM, length_remaining)
	key_exchange_one_only(TPM, TPM_other)
	return xor_strings(key, ciphertext)


y = TPM(500, 25, 1000)
x = TPM(500, 25, 1000)
synchronize(x, y, 500)

teststring = raw_input("Enter string to be encrypted: (Must be less than 500 characters):\n")
x_c = TPM(1, 1, 1)
y_c = TPM(1, 1, 1)
x.fullcopy(x_c)
y.fullcopy(y_c)
key_exchange_one_only(x_c, y_c)
testenc = encrypt(y, x_c, teststring)

print "Encrypted text is: ", testenc, "\n"
raw_input("Press enter to continue.")

new_plain = decrypt(x, y_c, testenc)
print "Decrypted text is: ", new_plain

