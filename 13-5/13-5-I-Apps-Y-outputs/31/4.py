
import math

def get_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB[0] * BC[1] - AB[1] * BC[0]
    Y = BC[0] * CD[1] - BC[1] * CD[0]
    return math.degrees(math.acos(X / math.sqrt(X**2 + Y**2)))

