import random
from TPM import *

input_size = 100
hidden_node_num = 10
weight_range = 100000



	

def input_generator():
	input_arr = []
	for y in xrange(input_size):
		input_arr.append(random.randint(-weight_range, weight_range))
	return input_arr

# Given two TPMs, it gives them a common output and calls the update function only if the outputs
# are equal.
def key_exchange(TPM1, TPM2):
	inputs = input_generator()
	out1 = TPM1.output(inputs)
	out2 = TPM2.output(inputs)
	if out1 == out2:
		#print "outputs the same"
		TPM1.hebbian_learning_rule(inputs, out1, out2)
		TPM2.hebbian_learning_rule(inputs, out2, out1)
		return 1
	return 0

# Takes two TPM's and runs key exchange until they have equal output for 
# cutoff number of times. 
# Choosing a good cutoff is very important! Too small of a cutoff and the machines
# may not be synchronized

def synchronize(TPM1, TPM2, cutoff):
	x = 0
	while x < cutoff:
		if key_exchange(TPM1, TPM2) == 1:   #goes until cutoff
			x+=1
		else:
			x-=1

# Checks if weights of two TPMs are actually secure. Run this after a synchronize
# call to make sure the weights are actually synced

def check_weights(TPM1, TPM2):
	for y in range(len(TPM1.weights)):
		if TPM1.weights[y] != TPM2.weights[y]:
			return -1
	return 0

	
	

