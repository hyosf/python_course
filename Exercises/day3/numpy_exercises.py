import numpy as np

def nullVector():
#a. Create a null vector of size 10 but the fifth value which is 1
    null_vector = np.zeros(10)
    null_vector[4] = 5
    print(null_vector)

def vector():
#b. Create a vector with values ranging from 10 to 49
    v = np.arange(10,50)
    print(v)

def reverse():
#c. Reverse a vector (first element becomes last)
    v = np.arange(0,10)
    v_reveresed = v[::-1]
    print(v_reveresed)
    print(v)

def matrix():
#d. Create a 3x3 matrix with values ranging from 0 to 8
    m = np.arange(0,9).reshape(3,3)
    print(m)

def find_indices():
#e. Find indices of non-zero elements from [1,2,0,0,4,0]
    r = np.array([1,2,0,0,4,0])
    indices = np.where(r != 0)
    print(indices)

find_indices()

def mean():
#f. Create a random vector of size 30 and find the mean value
    v = np.random.random(30)
    mean = np.mean(v)
    print(f'The mean of this vector is: {mean:.2f}')

def zeroBorders():
#g. Create a 2d array with 1 on the border and 0 inside
    array = np.ones([4,4])
    array[1:3,1:3] = 0
    print(array)

def checkerboard():
#h. Create a 8x8 matrix and fill it with a checkerboard pattern
    m = np.zeros((8,8))
    m[1::2, ::2] = 1
    m[::2, 1::2] = 1
    print(m)

def checkerboardTile():
#i. Create a checkerboard 8x8 matrix using the tile function
    m = np.array([[0, 1], [1 ,0]])
    mm = np.tile(m,(4,4))
    print(mm)

def negate():
#j. Given a 1D array, negate all elements which are between 3 and 8, in place
    Z = np.arange(11)
    # Z[4:9] = list(map(lambda x:-x, Z[4:9]))
    Z[4:9] = -Z[4:9]
    print(Z)

def sort():
#k. Create a random vector of size 10 and sort it
    Z = np.random.random(10)
    Z = np.sort(Z)
    print(Z)

def equal():
#l. Consider two random array A anb B, check if they are equal
    A = np.random.randint(0,2,5)
    B = np.random.randint(0,2,5)
    equal = np.array_equal(A,B)
    print(equal)

def squares():
#m. How to calculate the square of every number in an array in place (without creating temporaries)?
    Z = np.arange(10, dtype=np.int32)
    print(Z.dtype)
    print(Z)
    Z **= 2
    print(Z.dtype)
    print(Z)

def diagonal():
    #n. How to get the diagonal of a dot product?
    A = np.arange(9).reshape(3,3)
    B = A + 1
    C = np.dot(A,B)
    D = np.diagonal(C)
    print(D)
