
import math

def get_input():
    return list(map(float, input().split()))

def get_angle(A, B, C, D):
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
    CD = [D[0] - C[0], D[1] - C[1], D[2] - C[2]]
    X = [AB[1] * BC[2] - AB[2] * BC[1], AB[2] * BC[0] - AB[0] * BC[2], AB[0] * BC[1] - AB[1] * BC[0]]
    Y = [BC[1] * CD[2] - BC[2] * CD[1], BC[2] * CD[0] - BC[0] * CD[2], BC[0] * CD[1] - BC[1] * CD[0]]
    return math.degrees(math.acos((X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]) / (math.sqrt(X[0]**2 + X[1]**2 + X[2]**2) * math.sqrt(Y[0]**2 + Y[1]**2 + Y[2]**2))))

def main():
    A = get_input()
    B = get_input()
    C = get_input()
    D = get_input()
    print(get_angle(A, B, C, D))

if __name__ == '__main__':
    main()

