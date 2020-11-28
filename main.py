import sys
import numpy as np
import random

num = int(sys.argv[1])
maxnum = (num*num)

matrix = np.zeros(shape=(num, num))
generated = random.sample(range(0, maxnum), maxnum)

print(matrix)
print(generated)
