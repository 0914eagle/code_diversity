
import math

def get_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB.cross(BC)
    Y = BC.cross(CD)
    return math.degrees(math.acos(X.dot(Y) / (X.magnitude() * Y.magnitude())))

