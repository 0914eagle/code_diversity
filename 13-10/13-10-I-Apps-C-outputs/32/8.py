
def get_input():
    N = int(input())
    P = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]
    return N, P, X

def is_possible(N, P, X):
    color = [-1] * (N + 1)
    weight = [0] * (N + 1)
    color[1] = 0
    weight[1] = X[1]
    for i in range(2, N + 1):
        if color[i] == -1:
            color[i] = 1 - color[P[i]]
            weight[i] = X[i] - weight[P[i]]
        else:
            if color[i] == color[P[i]]:
                return False
            weight[i] = X[i] - weight[P[i]]
    return True

def main():
    N, P, X = get_input()
    if is_possible(N, P, X):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()

