import sys
import numpy as np
import random

num = int(sys.argv[1])
maxnum = (num*num)

generated = random.sample(range(0, maxnum), maxnum)

matrix = np.array(generated).reshape((num, num))

print(generated)
print('')
print(matrix)
