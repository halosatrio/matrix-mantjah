import random
import numpy as np

num = 10
maxnum = (num*num)

arr = random.sample(range(0, maxnum), maxnum)

matrix = np.array(arr).reshape((num, num))

# print("list: \n", arr, "\n")

print("matrix:")
print(matrix, "\n")

print("checking row:")


def check(row):
    hasil = []
    for i in range(len(row)):
        if i == len(row)-1:
            break
        if abs(row[i] - row[i+1]) == 1:
            hasil.append(False)
        else:
            hasil.append(True)
    if False in hasil:
        return False
    else:
        return True


def valid():
    global matrix
    for row in matrix:
        if check(row) == False:
            random.shuffle(row)
            valid()
        if check(row) == True:
            pass
    matrix = np.transpose(matrix)
    for row in matrix:
        if check(row) == False:
            random.shuffle(row)
            valid()
        if check(row) == True:
            pass


valid()
print(matrix, "\n")

# print('False')
# print('True')
# a = [False, False, False, False]
# b = [False, True, False, True]

# print("a == True? ", a == True)
# print("a == False? ", a == False)
# print("b == True? ", b == True)
# print("b == False? ", b == False)
