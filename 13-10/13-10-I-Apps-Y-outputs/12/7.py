
import math

def get_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C
    X = get_cross_product(AB, BC)
    Y = get_cross_product(BC, CD)
    dot_product = get_dot_product(X, Y)
    return math.degrees(math.acos(dot_product / (get_magnitude(X) * get_magnitude(Y))))

def get_dot_product(X, Y):
    return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]

def get_magnitude(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)

def get_cross_product(A, B):
    return [A[1] * B[2] - A[2] * B[1], A[2] * B[0] - A[0] * B[2], A[0] * B[1] - A[1] * B[0]]

if __name__ == '__main__':
    A = [float(x) for x in input().split()]
    B = [float(x) for x in input().split()]
    C = [float(x) for x in input().split()]
    D = [float(x) for x in input().split()]
    print(get_angle(A, B, C, D))

