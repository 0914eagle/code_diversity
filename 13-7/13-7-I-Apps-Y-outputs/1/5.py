
def get_input():
    return list(map(int, input().split()))

def solve(X, Y):
    for i in range(1, X+1):
        if X % i == 0:
            j = X // i
            if i + j == Y:
                return "Yes"
    return "No"

def main():
    X, Y = get_input()
    print(solve(X, Y))

if __name__ == '__main__':
    main()

