import random
import TPM

input_size = 10
hidden_node_num = 2
weight_range = 500

party1 = TPM(input_size, hidden_node_num, weight_range)
party2 = TPM(input_size, hidden_node_num, weight_range)

def input_controller(TPM1, TPM2):
	input_arr = []
	for xrange(input_size):
		input_arr.append(random.randint(-weight_range, weight_range))
	
