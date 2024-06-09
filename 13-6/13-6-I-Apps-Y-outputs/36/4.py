
def solve(K, X):
    if K * 500 >= X:
        return "Yes"
    else:
        return "No"

def main():
    K, X = map(int, input().split())
    print(solve(K, X))

if __name__ == '__main__':
    main()

