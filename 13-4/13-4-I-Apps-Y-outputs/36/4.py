
def get_input():
    return list(map(int, input().split()))

def solve(X, A):
    if X < A:
        return 0
    else:
        return 10

def main():
    X, A = get_input()
    print(solve(X, A))

if __name__ == '__main__':
    main()

