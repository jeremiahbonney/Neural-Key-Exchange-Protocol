import random
from TPM import *
from NKEP import *

cutoff = 30

x = TPM(100, 10, 100000)
#x.print_weights()
#x.output([1, 0, 1, -1, 1, 1, 0, -1])
y = TPM(100, 10, 100000)
#y.print_weights()
#y.output([1, 0, 1, -1, 1, 1, 0, -1])

#print input_generator()

synchronize(x, y, cutoff)
if check_weights(x, y) == -1:
	print "Weights not synced!"
else:
	print "Weights are synced!"


x.print_weights()
print "\n\n"
y.print_weights()
