import numpy as np
from PIL import Image

def addition(matrix1, matrix2):
    matrix3 = np.empty(matrix1.shape)
    rows, cols = matrix1.shape
    if(matrix1.shape!=matrix2.shape):
        print("Wrong dimensions of matrices")
        return
    for i in range(rows):
        for j in range(cols):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix3


def substraction(matrix1, matrix2):
    matrix3 = np.empty(matrix1.shape)
    rows, cols = matrix1.shape
    if(matrix1.shape!=matrix2.shape):
        print("Wrong dimensions of matrices")
        return
    for i in range(rows):
        for j in range(cols):
            matrix3[i][j] = matrix2[i][j] - matrix1[i][j]
    return matrix3


def multiplication(matrix1, matrix2):
    rows, cols = matrix1.shape
    rows2, col2 = matrix2.shape
    matrix3 = np.empty(matrix1.shape, dtype=int)
    if(cols!= rows2):
        print("Wrong dimensions")
        return
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

def image_to_matrix(image):
    img = Image.open(image)

    matrix_red = np.zeros((img.size[1],img.size[0]),dtype=int)
    matrix_green = np.zeros((img.size[1],img.size[0]),dtype=int)
    matrix_blue = np.zeros((img.size[1],img.size[0]),dtype=int)
    pixels = list(img.get_flattened_data())
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            matrix_red[i][j] = pixels[i*img.size[0]+j][0]
            matrix_green[i][j] = pixels[i*img.size[0]+j][1]
            matrix_blue[i][j] = pixels[i*img.size[0]+j][2]

    return matrix_red, matrix_green, matrix_blue


def matrix_to_image(matrix_red, matrix_green, matrix_blue):
    rows,cols = matrix_red.shape
    img = Image.new("RGB", (cols,rows))
    for i in range(rows):
        for j in range(cols):
            img.putpixel((j,i),(matrix_red[i][j], matrix_green[i][j], matrix_blue[i][j]))
    img.show()


if __name__ == '__main__':

    matrix_red,matrix_green,matrix_blue = image_to_matrix("2.bmp")

    matrix_to_image(matrix_red,matrix_green,matrix_blue)
    # print(multiplication(matrix1, matrix2))
    # print(transpose(matrix1))


