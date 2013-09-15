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
z = 0
counter = 0
while z in xrange(3000):
	if key_exchange(x, y) == 1:
		counter +=1
	else:
		counter = 0
	z+=1
	if counter >= 40:
		print "weights should be synced after ", z, "iterations."
		break

x.print_weights()
print "\n\n"
y.print_weights()
