
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
    cosine_angle = dot_product / (magnitude_X * magnitude_Y)
    angle = math.degrees(math.acos(cosine_angle))
    return angle

def cross_product(u, v):
    x = u[1] * v[2] - u[2] * v[1]
    y = u[2] * v[0] - u[0] * v[2]
    z = u[0] * v[1] - u[1] * v[0]
    return [x, y, z]

def dot_product(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]

def magnitude(u):
    return math.sqrt(dot_product(u, u))

if __name__ == '__main__':
    A = [float(x) for x in input().split()]
    B = [float(x) for x in input().split()]
    C = [float(x) for x in input().split()]
    D = [float(x) for x in input().split()]
    angle = get_angle(A, B, C, D)
    print(f"{angle:.2f}")

