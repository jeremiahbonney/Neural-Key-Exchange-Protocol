import random
from TPM import *

x = TPM(8, 4, 10000)
x.print_weights()
x.output([1, 0, 1, -1, 1, 1, 0, -1])