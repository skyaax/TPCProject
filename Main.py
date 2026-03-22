import numpy as np

def addition(matrix1, matrix2):
    matrix3 = np.empty(matrix1.shape)
    rows,cols = matrix1.shape
    for i in range(rows):
        for j in range(cols):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix3


def multiplication(matrix1, matrix2):
    


    return matrix3





if __name__ == '__main__':
    matrix1 = np.array([[1, 2], [4, 5]])
    matrix2 = np.array([[10, 10], [10, 10]])

    multiplication(matrix1, matrix2)



