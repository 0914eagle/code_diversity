
def get_input():
    return [float(x) for x in input().split()]

def get_angle(A, B, C):
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
    X = [AB[1] * BC[2] - AB[2] * BC[1], AB[2] * BC[0] - AB[0] * BC[2], AB[0] * BC[1] - AB[1] * BC[0]]
    Y = [BC[1] * X[2] - BC[2] * X[1], BC[2] * X[0] - BC[0] * X[2], BC[0] * X[1] - BC[1] * X[0]]
    return math.degrees(math.acos((X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]) / (math.sqrt(X[0]**2 + X[1]**2 + X[2]**2) * math.sqrt(Y[0]**2 + Y[1]**2 + Y[2]**2))))

def main():
    A, B, C, D = get_input()
    print(get_angle(A, B, C))

if __name__ == '__main__':
    main()

