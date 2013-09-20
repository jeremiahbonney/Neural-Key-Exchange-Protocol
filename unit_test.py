import random
from TPM import *
from NKEP import *

# These first few functions test the basic functions of TPMs, to make sure they work correctly.

# big_theta test
def big_theta_test():
	assert big_theta(1, 1) == 1
	assert big_theta(0, 1) == 0
	assert big_theta(1, 0) == 0
	print "big_theta test passed"

def print_weights_test():
	x = TPM(5, 2, 10)
	x.weights = [1,2,1,2,1]
	x.print_weights() #Check this by seeing what it prints out
	print "print_weights_test passed? Look to check for sure."


#Tests the NKEP functions

#Tests check_weights function
def check_weights_test():
	x = TPM(10, 5, 5)
	y = TPM(10, 5, 5)
	x.weights= [1,1,1,1,1,1,1,1,1,1]
	y.weights= [1,1,1,1,1,1,1,1,1,1]

	assert check_weights(x,y) == 0
	y.weights = [0,0,0,0,0,0,0,0,0,0]

	assert check_weights(x, y) == -1

	y.weights = [1,1,1,1,0,1,1,1,1,1]
	assert check_weights(x, y) == -1
	print "check_weights_test passed"

#Tests input generator function
def input_generator_test():
	input_size = 30
	weight_range = 1000
	counter = 0
	for z in range(20):
		for element in input_generator(input_size, weight_range):
			assert element <= weight_range
			assert element >= -weight_range
			counter +=1
		assert counter == input_size
		counter = 0

	print "input_generator_test passed"

'''
def key_exchange_test():
	x = TPM(2, 1, 50)
	y = TPM(2, 1, 50)
	x.weights = [1,0]
	y.weights == x.weights
	assert key_exchange(x, y) == 1
	x.weights = [1, 0]
	y.weights = [0, 0]
	assert key_exchange(x, y) == 0

	print "key_exchange_test passed"
'''

# Work on better test for this function
def synchronize_test():
	x = TPM(10, 2, 50)
	y = TPM(10, 2, 50)
	cutoff = 10
	assert synchronize(x, y, cutoff) == 0
	print "synchronize_test passed"


def test_all():
	big_theta_test()
	print_weights_test()
	check_weights_test()
	input_generator_test()
	#key_exchange_test()
	synchronize_test()
	print "\nAll tests passed!"

test_all()