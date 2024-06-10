
import math

def get_angle(A, B, C, D):
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
    CD = [D[0] - C[0], D[1] - C[1], D[2] - C[2]]
    X = cross_product(AB, BC)
    Y = cross_product(BC, CD)
    dot_product = dot_product(X, Y)
    magnitude_X = magnitude(X)
    magnitude_Y = magnitude(Y)
    cos_phi = dot_product / (magnitude_X * magnitude_Y)
    phi = math.acos(cos_phi) * 180 / math.pi
    return phi

def cross_product(a, b):
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    return [x, y, z]

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def magnitude(a):
    return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)

if __name__ == '__main__':
    A = [float(x) for x in input().split()]
    B = [float(x) for x in input().split()]
    C = [float(x) for x in input().split()]
    D = [float(x) for x in input().split()]
    print(get_angle(A, B, C, D))

