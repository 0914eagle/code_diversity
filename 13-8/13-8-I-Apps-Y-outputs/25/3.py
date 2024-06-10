
def get_input():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    return N, M, X, Y, x, y

def solve(N, M, X, Y, x, y):
    # Find the minimum of x and y
    min_val = min(x + y)
    # Check if the minimum value is between X and Y
    if X < min_val <= Y:
        return "No War"
    else:
        return "War"

def main():
    N, M, X, Y, x, y = get_input()
    print(solve(N, M, X, Y, x, y))

if __name__ == '__main__':
    main()

