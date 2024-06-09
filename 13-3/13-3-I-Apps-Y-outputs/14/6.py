
import math

def get_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB.cross(BC)
    Y = BC.cross(CD)
    cos_phi = X.dot(Y) / (AB.length() * BC.length() * CD.length())
    return math.degrees(math.acos(cos_phi))

def main():
    A = Vector3(map(float, input().split()))
    B = Vector3(map(float, input().split()))
    C = Vector3(map(float, input().split()))
    D = Vector3(map(float, input().split()))
    print(get_angle(A, B, C, D))

if __name__ == '__main__':
    main()

