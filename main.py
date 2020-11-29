import sys
import numpy as np
import random

num = int(sys.argv[1])
maxnum = (num*num)

# generate list with unique random number in range 0 to (num*num)-1
generated = random.sample(range(0, maxnum), maxnum)

# define max digit on the list
maxdigit = len(str(maxnum-1))

matrix = np.array(generated).reshape((num, num))


# fungsi cek dan benerin rows
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


# fungsi cek validnya
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

# def valid():
#     global matrix
#     for row in matrix:
#         if check(row) == False:
#             print('False')
#         if check(row) == True:
#             print('True')


# print the output aesthetically
if num >= 5:
    valid()
    decimal = []
    hasil = matrix.reshape((1, maxnum))[0]
    for i in hasil:
        decimal.append(str(i).zfill(maxdigit))

    # generate matrix num x num
    final = np.array(decimal).reshape((num, num))
    print('\n'.join(['  '.join([str(cell) for cell in row])
                     for row in final]))
else:
    # change each number on the list into decimal.
    decimal = []
    for i in generated:
        decimal.append(str(i).zfill(maxdigit))

    # generate matrix num x num
    matrix = np.array(decimal).reshape((num, num))
    print('\n'.join(['  '.join([str(cell) for cell in row])
                     for row in matrix]))
