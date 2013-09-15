import random
from TPM import *
from NKEP import *

x = TPM(30, 5, 10000)
#x.print_weights()
#x.output([1, 0, 1, -1, 1, 1, 0, -1])
y = TPM(30, 5, 10000)
#y.print_weights()
#y.output([1, 0, 1, -1, 1, 1, 0, -1])

#print input_generator()

counter = 0
count = 0
while counter < 40:
	if key_exchange(x, y) == 1:
		counter +=1
	else:
		counter = 0
	count +=1

	
print "weights should be synced after ", count , "iterations"

x.print_weights()
print "\n\n"
y.print_weights()
