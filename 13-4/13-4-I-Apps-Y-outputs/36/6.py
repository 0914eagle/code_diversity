
def read_input():
    return [int(x) for x in input().split()]

def solve(X, A):
    if X < A:
        return 0
    else:
        return 10

def main():
    X, A = read_input()
    print(solve(X, A))

if __name__ == '__main__':
    main()

