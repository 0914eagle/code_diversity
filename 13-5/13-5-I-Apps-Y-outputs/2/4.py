
def get_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB x BC
    Y = BC x CD
    return np.arccos((X.Y)/(np.linalg.norm(X)*np.linalg.norm(Y)))*180/np.pi

def main():
    A = np.array([float(x) for x in input().split()])
    B = np.array([float(x) for x in input().split()])
    C = np.array([float(x) for x in input().split()])
    D = np.array([float(x) for x in input().split()])
    print(get_angle(A, B, C, D))

if __name__ == '__main__':
    main()

