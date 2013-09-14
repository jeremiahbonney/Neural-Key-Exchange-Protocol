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
		self.hidden_node_num = hidden_node_num
		random.seed()
		for x in xrange(input_num):
			self.weights.append(random.randint(-weight_range, weight_range))

	def output(self, input_arr):
		step2_arr = []
		step_sum = 0
		counter = 0
		result = 1
		for x in xrange(len(input_arr)):
			step_sum+=input_arr[x] * self.weights[x]
			if x % (self.input_num/self.hidden_node_num) != 0:
				if step_sum > 0:
					step2_arr.append(1)
				elif step_sum == 0:
					step2_arr.append(0)
				else:
					step2_arr.append(-1)
				step_sum = 0


		for y in step2_arr:
			#print "step2_arr value is ", y
			result *= y

		if result == 0:
			result = -1

		print result, "result"
		return result

	def print_weights(self):
		for x in self.weights:
			print x




