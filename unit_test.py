import random
from TPM import *
from NKEP import *

cutoff = 10

x = TPM(100, 10, 100000)
#x.print_weights()
#x.output([1, 0, 1, -1, 1, 1, 0, -1])
y = TPM(100, 10, 100000)
#y.print_weights()
#y.output([1, 0, 1, -1, 1, 1, 0, -1])

#print input_generator()

synchronize(x, y, cutoff)
for z in xrange(x.input_num):
	if x.weights[z] != y.weights[z]:
		print "Error! Weight number ", z, "is not the same for both machines!"


x.print_weights()
print "\n\n"
y.print_weights()
