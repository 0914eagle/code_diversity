
import math

def get_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB.cross(BC)
    Y = BC.cross(CD)
    cos_phi = X.dot(Y) / (X.length() * Y.length())
    return math.degrees(math.acos(cos_phi))

