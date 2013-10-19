import random
from TPM import *

#input_size = 100
#hidden_node_num = 10
#weight_range = 100000



	

def input_generator(input_size, weight_range):
	input_arr = []
	for y in xrange(input_size):
		input_arr.append(random.randint(-weight_range, weight_range))
	return input_arr

# Given two TPMs, it gives them a common output and calls the update function only if the outputs
# are equal.
def key_exchange(TPM1, TPM2):
	inputs = input_generator(TPM1.input_num, TPM1.weight_range)
	out1 = TPM1.output(inputs)
	out2 = TPM2.output(inputs)
	if out1 == out2:
		#print "outputs the same"
		TPM1.hebbian_learning_rule(inputs, out1, out2)
		TPM2.hebbian_learning_rule(inputs, out2, out1)
		return 1
	return 0

def key_exchange_one_only(TPM1, TPM2):
	inputs = input_generator(TPM1.input_num, TPM1.weight_range)
	out1 = TPM1.output(inputs)
	out2 = TPM2.output(inputs)
	if out1 == out2:
		#print "outputs the same"
		TPM1.hebbian_learning_rule(inputs, out1, out2)
		#TPM2.hebbian_learning_rule(inputs, out2, out1)
		return 1
	return 0


# Takes two TPM's and runs key exchange until they have equal output for 
# cutoff number of times. 
# Choosing a good cutoff is very important! Too small of a cutoff and the machines
# may not be synchronized, but too large and "evesdroppers" may be able to sync as well.

def synchronize(TPM1, TPM2, cutoff):
	x = 0
	while x < cutoff:
		if key_exchange(TPM1, TPM2) == 1:   #goes until cutoff
			x+=1
		else:
			x-=1
	return 0

# Checks if weights of two TPMs are actually secure. Run this after a synchronize
# call to make sure the weights are actually synced

def check_weights(TPM1, TPM2):
	for y in range(len(TPM1.weights)):
		if TPM1.weights[y] != TPM2.weights[y]:
			return -1
	return 0


# This function actually runs the key exchange, prompting the users for input and then 
# runs the key exchange until the weights are synced.

def nkep():
	input_size = int(raw_input("Enter the desired number of inputs for the networks\n"))
	hidden_node_num = int(raw_input("Enter the desired number of hidden nodes. Must be able to divide the input size.\n"))
	weight_range = int(raw_input("What weight range would you like to use? Note: Enter only one number, the range will be made up of the positive and negative versions of that number.\n"))
	cutoff = int(raw_input("Enter a cutoff for the number of correct outputs needed to be synchronized:\n"))
	x = TPM(input_size, hidden_node_num, weight_range)
	y = TPM(input_size, hidden_node_num, weight_range)

	while check_weights(x, y) < 0:
		synchronize(x, y, cutoff)

	print "Weights are now synced, printing them now\n"
	print "First TPM's weights"
	x.print_weights()
	print "\n"
	print "Second TPM's weights"
	y.print_weights()




	
	

