import numpy as np


def addition(matrix1, matrix2):
    matrix3 = np.empty(matrix1.shape)
    rows, cols = matrix1.shape
    for i in range(rows):
        for j in range(cols):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix3


def substraction(matrix1, matrix2):
    matrix3 = np.empty(matrix1.shape)
    rows, cols = matrix1.shape
    for i in range(rows):
        for j in range(cols):
            matrix3[i][j] = matrix2[i][j] - matrix1[i][j]
    return matrix3


def multiplication(matrix1, matrix2):
    rows, cols = matrix1.shape
    matrix3 = np.empty(matrix1.shape)
    for i in range(rows):
        for j in range(cols):
            for k in range(cols):
                matrix3[i][j] += matrix1[i][k] * matrix2[i][k]

    return matrix3


def transpose(matrix):
    rows, cols = matrix.shape
    matrix_new = np.zeros([cols, rows])
    for i in range(rows):
        for j in range(cols):
            matrix_new[j][i] = matrix[i][j]
    return matrix_new


def scalar(matrix, scalar):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] *= scalar
    return matrix


if __name__ == '__main__':
    matrix1 = np.array([[1, 2, 3], [4, 5, 7]])
    matrix2 = np.array([[10, 10], [10, 10]])

    # print(multiplication(matrix1, matrix2))
    # print(transpose(matrix1))



