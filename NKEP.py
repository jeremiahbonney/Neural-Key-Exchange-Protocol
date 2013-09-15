import random
from TPM import *

input_size = 30
hidden_node_num = 5
weight_range = 10000

def big_theta(a, b):
	if(a==b):
		return 1
	else:
		return 0
def hebbian_learning_rule(TPM1, TPM2, inputs, out1, out2):
	
	for x in xrange(input_size):
		TPM1.weights[x] += TPM1.step2_arr[x/hidden_node_num]*inputs[x]*big_theta(TPM1.step2_arr[x/hidden_node_num], out1)*big_theta(out1, out2)
		TPM2.weights[x] += TPM2.step2_arr[x/hidden_node_num]*inputs[x]*big_theta(TPM2.step2_arr[x/hidden_node_num], out2)*big_theta(out2, out1)
		if TPM1.weights[x] > weight_range:
			TPM1.weights[x] = weight_range

		if TPM1.weights[x] < -weight_range:
			TPM1.weights[x] = -weight_range

		if TPM2.weights[x] > weight_range:
			TPM2.weights[x] = weight_range

		if TPM2.weights[x] < -weight_range:
			TPM2.weights[x] = -weight_range



def anti_hebbian_learning_rule(TPM1, TPM2):
	for x in xrange(input_size):
		TPM1.weights[x] -= TPM1.step2_arr[x/hidden_node_num]*inputs[x]*big_theta(TPM1.step2_arr[x/hidden_node_num], out1)*big_theta(out1, out2)
		TPM2.weights[x] -= TPM2.step2_arr[x/hidden_node_num]*inputs[x]*big_theta(TPM2.step2_arr[x/hidden_node_num], out2)*big_theta(out2, out1)


def random_walk(TPM1, TPM2):
	for x in xrange(input_size):
		TPM1.weights[x] += inputs[x]*big_theta(TPM1.step2_arr[x/hidden_node_num], out1)*big_theta(out1, out2)
		TPM2.weights[x] += inputs[x]*big_theta(TPM2.step2_arr[x/hidden_node_num], out2)*big_theta(out2, out1)

	
learning_func = hebbian_learning_rule

party1 = TPM(input_size, hidden_node_num, weight_range)
party2 = TPM(input_size, hidden_node_num, weight_range)

def input_generator():
	input_arr = []
	for y in xrange(input_size):
		input_arr.append(random.randint(-weight_range, weight_range))
	return input_arr

def key_exchange(TPM1, TPM2):
	inputs = input_generator()
	out1 = TPM1.output(inputs)
	out2 = TPM2.output(inputs)
	if out1 == out2:
		#print "outputs the same"
		learning_func(TPM1, TPM2, inputs, out1, out2)
		return 1
	return 0




