
def get_input():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    return N, M, X, Y, x, y

def solve(N, M, X, Y, x, y):
    # Check if X < Z <= Y
    for Z in range(X+1, Y+1):
        # Check if x_1, x_2, ..., x_N < Z
        if all(xi < Z for xi in x):
            # Check if y_1, y_2, ..., y_M >= Z
            if all(yi >= Z for yi in y):
                return "No War"
    return "War"

def main():
    N, M, X, Y, x, y = get_input()
    print(solve(N, M, X, Y, x, y))

if __name__ == '__main__':
    main()

