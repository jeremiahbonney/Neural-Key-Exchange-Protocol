import random

class TPM:
	input_num = 0
	hidden_node_num = 0
	weight_range = 0
	weights = []

	def __init__(self, input_num, hidden_node_num, weight_range):
		while input_num % hidden_node_num != 0:
			input_num += 1
		self.input_num = input_num
		self.weight_range = weight_range
		random.seed()
		for x in range(0, input_num):
			self.weights.append(random.randint(-weight_range, weight_range))

	def output(input_arr):
		step2_arr = []
		step_sum = 0
		counter = 0
		result = 0
		for x in range(0, len(input_arr)):
			step_sum+=input_arr[x] * weights[x]
			if x != 0 and x%hidden_node_num == 0:
				if step_sum > 0:
					step2_arr[counter] = 1
				elif step_sum == 0:
					step2_arr[counter] = 0
				else:
					step2_arr[counter] = -1
				counter += 1 
				step_sum = 0

		for y in step_arr:
			result *= y

		if result == 0:
			result = -1

		return result




