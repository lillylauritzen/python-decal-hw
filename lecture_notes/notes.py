import numpy as np
arr = np.zeros((2, 5))
arr
array([[0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.]])

""" creates an array with 0s of the given dimensions
arr = np.zeros((3,3))

arr = np.zeros((2, 5))
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if (i + j) % 2 == 0:
            arr[i, j] = 1

        """

