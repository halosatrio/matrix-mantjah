import random
import numpy as np

num = 3
maxnum = (num*num)

row = random.sample(range(0, maxnum), maxnum)

matrix = np.array(row).reshape((num, num))

hasil = matrix.reshape((1, maxnum))[0]

print(row, "\n")

print(matrix, "\n")

print(hasil, "\n")


def valid(row):
    hasil = []
    for i in range(len(row)):
        if i == len(row)-1:
            break
        if abs(row[i] - row[i+1]) == 1:
            hasil.append(False)
        else:
            hasil.append(True)
    print(hasil)
    if False in hasil:
        print('False')
    else:
        print('True')


valid(row)

# print('False')
# print('True')
# a = [False, False, False, False]
# b = [False, True, False, True]

# print("a == True? ", a == True)
# print("a == False? ", a == False)
# print("b == True? ", b == True)
# print("b == False? ", b == False)
