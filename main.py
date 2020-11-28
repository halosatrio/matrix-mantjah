import sys
import numpy as np
import random

num = int(sys.argv[1])
maxnum = (num*num)

# generate list with unique random number in range 0 to (num*num)-1
generated = random.sample(range(0, maxnum), maxnum)

# define max digit on the list
maxdigit = len(str(maxnum-1))

# change each number on the list into decimal.
decimal = []
for i in generated:
    decimal.append(str(i).zfill(maxdigit))

# generate matrix num x num
matrix = np.array(decimal).reshape((num, num))

# print the output aesthetically
print('\n'.join(['  '.join([str(cell) for cell in row]) for row in matrix]))
