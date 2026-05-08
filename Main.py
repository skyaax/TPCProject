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
    rows2, cols2 = matrix2.shape
    if(cols != rows2):
        print("Wrong dimensions")
        return

    matrix3 = np.zeros((rows, cols2))
    for i in range(rows):
        for j in range(cols2):
            for k in range(cols):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

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
    img = Image.open(image).convert("RGB")

    matrix_red = np.zeros((img.size[1],img.size[0]),dtype=int)
    matrix_green = np.zeros((img.size[1],img.size[0]),dtype=int)
    matrix_blue = np.zeros((img.size[1],img.size[0]),dtype=int)
    pixels = list(img.getdata())
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
            img.putpixel((j,i),(int(matrix_red[i][j]), int(matrix_green[i][j]), int(matrix_blue[i][j])))
    img.show()

def rotate_matrix(matrix, point, angle_degrees):
    angle_radians = np.deg2rad(angle_degrees)
    cos_angle = np.cos(angle_radians)
    sin_angle = np.sin(angle_radians)
    inverse_rotation = np.array([[cos_angle, sin_angle], [-sin_angle, cos_angle]])
    pivot_x, pivot_y = point
    rows, cols = matrix.shape
    new_matrix = np.zeros_like(matrix)

    for y in range(rows):
        for x in range(cols):
            v = np.array([[x - pivot_x], [y - pivot_y]])
            old_x, old_y = multiplication(inverse_rotation, v).flatten()
            old_x = int(round(old_x + pivot_x))
            old_y = int(round(old_y + pivot_y))

            if 0 <= old_x < cols and 0 <= old_y < rows:
                new_matrix[y][x] = matrix[old_y][old_x]

    return new_matrix


def scale_matrix(matrix,scale_factor):
    if scale_factor <= 0:
        print("Scale factor must be greater than 0")
        return

    rows,cols = matrix.shape
    new_rows,new_cols = int(scale_factor*rows),int(scale_factor*cols)
    new_matrix = np.zeros((new_rows,new_cols),dtype=matrix.dtype)
    for y in range(new_rows):
        for x in range(new_cols):
            old_x = int(x/scale_factor)
            old_y = int(y/scale_factor)
            if 0 <= old_x < cols and 0 <= old_y < rows:
                new_matrix[y][x] = matrix[old_y][old_x]
    return new_matrix
                        
def skew_matrix(matrix,skew_x,skew_y):
    rows,cols = matrix.shape
    corners = [(0,0),(cols-1,0),(0,rows-1),(cols-1,rows-1)]
    skewed_corners = []

    for x,y in corners:
        new_x = x + skew_x*y
        new_y = skew_y*x + y
        skewed_corners.append((new_x,new_y))

    min_x = int(np.floor(min(x for x,y in skewed_corners)))
    max_x = int(np.ceil(max(x for x,y in skewed_corners)))
    min_y = int(np.floor(min(y for x,y in skewed_corners)))
    max_y = int(np.ceil(max(y for x,y in skewed_corners)))

    new_cols = max_x - min_x + 1
    new_rows = max_y - min_y + 1
    new_matrix = np.zeros((new_rows,new_cols),dtype=matrix.dtype)

    determinant = 1 - skew_x*skew_y
    if np.isclose(determinant, 0):
        print("Skew matrix cannot be inverted")
        return

    inverse_skew = (1/determinant) * np.array([
        [1,-skew_x],
        [-skew_y,1]
    ])

    for y in range(new_rows):
        for x in range(new_cols):
            v=np.array([[x + min_x],[y + min_y]])
            old_x, old_y = multiplication(inverse_skew, v).flatten()
            old_x = int(round(old_x))
            old_y = int(round(old_y))
            if 0 <= old_x < cols and 0 <= old_y < rows:
                new_matrix[y][x] = matrix[old_y][old_x]
    return new_matrix

def to_grayscale(matrix_red,matrix_green,matrix_blue):
    matrix_new = np.zeros_like(matrix_red)
    rows,cols = matrix_red.shape
    for y in range(rows):
        for x in range(cols):
            I = 0.299*matrix_red[y][x]+0.587*matrix_green[y][x]+0.114*matrix_blue[y][x]
            matrix_new[y][x] = I
    return matrix_new.astype(np.uint8)

def edge_detection(matrix):
    matrix_new = np.zeros_like(matrix,dtype=np.uint16)
    rows,cols = matrix.shape
    diff = 25
    for y in range(1,rows-1):
        for x in range(1,cols-1):
            pixel = int(matrix[y][x])
            right = int(matrix[y][x+1])
            down = int(matrix[y+1][x])
            down_right = int(matrix[y+1][x+1])
            up_right = int(matrix[y-1][x+1])
            if abs(pixel - right)>=diff or abs(pixel - down)>=diff or abs(pixel - down_right)>=diff or abs(pixel - up_right)>=diff:
                matrix_new[y][x] = 255
            else:
                matrix_new[y][x] = 0
    return matrix_new.astype(np.uint8)

if __name__ == '__main__':

    matrix_red,matrix_green,matrix_blue = image_to_matrix("2.bmp")
    rows,cols = matrix_blue.shape
    
    #matrix_red_rotated = rotate_matrix(matrix_red,(cols//2,rows//2),90)
    #matrix_green_rotated = rotate_matrix(matrix_green,(cols//2,rows//2),90)
    #matrix_blue_rotated = rotate_matrix(matrix_blue,(cols//2,rows//2),90)
    #matrix_to_image(matrix_red_rotated,matrix_green_rotated,matrix_blue_rotated)
    
    #matrix_red_new = scale_matrix(matrix_red,2)
    #matrix_green_new = scale_matrix(matrix_green,2)
    #matrix_blue_new = scale_matrix(matrix_blue,2)
    #matrix_to_image(matrix_red_new,matrix_green_new,matrix_blue_new)
    
    #red_skew = skew_matrix(matrix_red,2,0)
    #green_skew = skew_matrix(matrix_green,2,0)
    #blue_skew = skew_matrix(matrix_blue,2,0)
    #matrix_to_image(red_skew,green_skew,blue_skew)
    
    
    #grayscale_array = (to_grayscale(matrix_red,matrix_green,matrix_blue))
    #print(grayscale_array)
    #img=Image.fromarray(grayscale_array)
    #img.show()
    
    #edge = edge_detection(grayscale_array)
    #img = Image.fromarray(edge)
    #img.show()
    
    #matrix_red = np.array([[58,84,199,36,1],[93,66,25,189,20]])
    #matrix_green = np.array([[27,48,3,7,60], [81,85,32,10,57]])
    #matrix_blue = np.array([[44,33,55,66,77], [88,99,110,140,248]])
    #matrix_to_image(matrix_red,matrix_green,matrix_blue)
    # print(multiplication(matrix1, matrix2))
    # print(transpose(matrix1))
