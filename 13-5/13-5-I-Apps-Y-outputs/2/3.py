
import math

def get_input():
    return list(map(float, input().split()))

def get_angle(A, B, C, D):
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
    CD = [D[0] - C[0], D[1] - C[1], D[2] - C[2]]
    X = get_cross_product(AB, BC)
    Y = get_cross_product(BC, CD)
    dot_product = get_dot_product(X, Y)
    magnitude_X = get_magnitude(X)
    magnitude_Y = get_magnitude(Y)
    cos_phi = dot_product / (magnitude_X * magnitude_Y)
    return math.degrees(math.acos(cos_phi))

def get_cross_product(A, B):
    return [A[1] * B[2] - A[2] * B[1], A[2] * B[0] - A[0] * B[2], A[0] * B[1] - A[1] * B[0]]

def get_dot_product(A, B):
    return A[0] * B[0] + A[1] * B[1] + A[2] * B[2]

def get_magnitude(A):
    return math.sqrt(A[0] ** 2 + A[1] ** 2 + A[2] ** 2)

if __name__ == '__main__':
    A = get_input()
    B = get_input()
    C = get_input()
    D = get_input()
    print(get_angle(A, B, C, D))

