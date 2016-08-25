import numpy as np
import timeit

print('------------- Part 1 -------------')
lst = [2, 3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
v = np.array(lst)
v + 2
print(v)
print(v * 2.2)
print(v - 1.38)
print(v ** 2)
print(v ** 1.5)

lst = [2, 3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
res = []
for val in lst:
    res.append(val + 2)
print(res)

print('')
print('------------- Part 2 -------------')
A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33]])
B = np.ones((3, 3))
print(A + B)
print(A * (B + 1))

print(np.dot(A, B))

print('')
print('------------- Part 3 -------------')
print(np.dot(3, 4))
x = np.array([3])
y = np .array([4])
print(x.ndim)
print(np.dot(x, y))
x = np.array([3, -2])
y = np.array([-4, 1])
print(np.dot(x, y))

A = np.array([[1, 2, 3], [3, 2, 1]])
B = np.array([[2, 3, 4, -2], [1, -1, 2, 3], [1, 2, 3, 0]])
print(A.shape[-1] == B.shape[-2], A.shape[1])
print(np.dot(A, B))

print('------------- Part 4 --------------')
X = np.array( [[[3,1, 2],
                [4, 2, 2],
                [3, 2, 2]],

               [[3, 2, 2],
                [4, 4, 3],
                [4, 1, 1]],

               [[2, 2, 1],
                [3, 1, 3],
                [3, 2, 3]]])

Y = np.array([[[2, 3, 1],
               [2, 2, 4],
               [3, 4, 4]],

              [[1, 4, 1],
               [4, 1, 2],
               [4, 1, 2]],

              [[1, 2, 3],
               [4, 1, 1],
               [3, 1, 4]]])

R = np.dot(X, Y)
print("The shapes: ")
print(X.shape)
print(Y.shape)
print(R.shape)
print("\nThe Result R:")
print(R)

print('')
print('--------------- Part 5 -----------')
X = np.array([[[3, 1, 2],
               [3, 2, 2]],

              [[-1, 0, 2],
               [1, -1, -2]],

              [[3, 2, 2],
               [4, 4, 3]],

              [[2, 2, 1],
               [3, 1, 3]]])
Y = np.array([[[2, 3, 1, 2, 1],
               [2, 2, 2, 0, 0],
               [3, 4, 0, 1, -1]],

              [[1, 4, 3, 2, 2],
                [4, 1, 1, 4, -3],
                [4, 1, 0, 3, 0]]])
R = np.dot(X, Y)
print("X.shape: ", X.shape, "   X.ndim", X.ndim)
print("Y.shape: ", Y.shape, "   Y.ndim", Y.ndim)

print("R.shape: ", R.shape, "   R.ndim: ", R.ndim)
print("\nThe result array R:\n")
print(R)

i=0
for j in range(X.shape[1]):
    for k in range(Y.shape[0]):
        for m in range(Y.shape[2]):
            fmt = " sum(X[{}, {}, :] * Y[{}, {}]) : {})"
            arguments = (i, j, k, m, sum(X[i, j, :] * Y[k, :, m]))
            print(fmt.format(*arguments))

print('')
print(R[0])
print('')

R2 = np.zeros(R.shape, dtype=np.int)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        for k in range(Y.shape[0]):
            for m in range(Y.shape[2]):
                R2[i, j, k, m] = sum(X[i, j, :] * Y[k, :, m])
print(np.array_equal(R, R2))
