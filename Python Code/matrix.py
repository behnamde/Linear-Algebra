import numpy as np

# Error
# A = [[1, 2, 4], [3, 4, 4], [4, 5, 5]]
# B = [[5, 3], [2, 8]]

# AB vector
A = np.ones((6, 7))
B = np.ones((7, 26)) * 2

# BA vector
# A = np.ones((7, 12))
# B = np.ones((6, 7)) * 14

print(' A = {}, \n\n B = {}'.format(A, B))

A_col = len(A)
A_row = len(A[0])
B_col = len(B)
B_row = len(B[0])

print('\nA({}x{})'.format(A_col, A_row))
print('B({}x{})\n'.format(B_col, B_row))


if A_row == B_col:
    pd = np.matmul(A, B)
    print('AB(using numpy.matmul function) = {}'.format(pd))
    pd = np.zeros((A_col, B_row))
    for i in range(A_col):
        for j in range(B_row):
            for k in range(B_col):
                pd[i][j] += A[i][k] * B[k][j]
    print('\nAB(using for loop) = {}'.format(pd))
elif B_row == A_col:
    pd = np.matmul(B, A)
    print('BA(using numpy.matmul function) = {}'.format(pd))
    pd = np.zeros((B_col, A_row))
    for i in range(B_col):
        for j in range(A_row):
            for k in range(A_col):
                pd[i][j] += B[i][k] * A[k][j]
    print('\nBA(using for loop) = {}'.format(pd))
else:
    print("""\n>> Vector XY(mxn) is available if and only if matrices X(mxp) and Y(pxn) exist
Here we have matrices A({}x{}) and B({}x{}) which are not match to definition\n""".format(A_col, A_row, B_col, B_row))