import random

class TMP:
	input_num = 0
	weight_range = 0
	weights = []

	def __init__(self, input_num, weight_range):
		if input_num % 2 != 0:
			input_num += 1
		self.input_num = input_num
		self.weight_range = weight_range
		random.seed()
		for x in range(0, input_num):
			weights + random.randint(-weight_range, weight_range)

	def output(input):


