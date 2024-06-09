
import math

def f1(A, B, C, D):
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
    CD = [D[0] - C[0], D[1] - C[1], D[2] - C[2]]
    X = [AB[1] * BC[2] - AB[2] * BC[1], AB[2] * BC[0] - AB[0] * BC[2], AB[0] * BC[1] - AB[1] * BC[0]]
    Y = [BC[1] * CD[2] - BC[2] * CD[1], BC[2] * CD[0] - BC[0] * CD[2], BC[0] * CD[1] - BC[1] * CD[0]]
    dot_product = X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]
    magnitude_X = math.sqrt(X[0] ** 2 + X[1] ** 2 + X[2] ** 2)
    magnitude_Y = math.sqrt(Y[0] ** 2 + Y[1] ** 2 + Y[2] ** 2)
    cosine_angle = dot_product / (magnitude_X * magnitude_Y)
    angle = math.degrees(math.acos(cosine_angle))
    return angle

def f2(...):
    ...

if __name__ == '__main__':
    A = [float(x) for x in input().split()]
    B = [float(x) for x in input().split()]
    C = [float(x) for x in input().split()]
    D = [float(x) for x in input().split()]
    print(f1(A, B, C, D))

