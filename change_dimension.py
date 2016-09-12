import numpy as np

print('------------- Part 1 ------------')
A = np.array([[[ 0,  1],
               [ 2,  3],
               [ 4,  5],
               [ 6,  7]],
              [[ 8,  9],
               [10, 11],
               [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])
Flattened_X = A.flatten()
print(Flattened_X)
print(A.flatten(order="C"))
print(A.flatten(order="F"))
print(A.flatten(order="A"))

print(A.ravel())
print(A.ravel(order="A"))
print(A.ravel(order="F"))
print(A.ravel(order="C"))
print(A.ravel(order="K"))

X = np.array(range(24))
Y = X.reshape((3, 4, 2))
print(Y)

print('')
print('---------------- Part 2 --------------')
x = np.array([11, 22])
y = np.array([18, 7, 6])
z = np.array([1, 3, 5])
c = np.concatenate((x, y, z))
print(c)

x = np.array(range(24))
x = x.reshape((3, 4, 2))
y = np.array(range(100, 124))
y = y.reshape((3, 4, 2))
z = np.concatenate((x, y))
print(z)
z = np.concatenate((x, y), axis=1)
print(z)

print('')
print('---------------- Part 3 --------------')
x = np.array([2, 5, 18, 14, 4])
y = x[:, np.newaxis]
print(y)

print('')
print('---------------- Part 4 --------------')
A = np.array([3, 4, 5])
B = np.array([1, 9, 0])
print(np.row_stack((A, B)))
print(np.column_stack((A, B)))
np.shape(A)

A = np.array([[3, 4, 5],
              [1, 9, 0],
              [4, 6, 8]])
print(np.column_stack((A, A, A)))
print(np.column_stack((A[0], A[0], A[0])))
print(np.dstack((A, A, A)))

print('')
print('--------------- Part 5 --------------')
x = np.array([[1, 2], [3, 4]])
print(np.tile(x, (3, 4)))

x = np.array([3.4])
y = np.tile(x, (5,))
print(y)

x = np.array([[1, 2], [3, 4]])
print(np.tile(x , 2))
print(np.tile(x, (2, 1)))
print(np.tile(x, (2, 2)))
