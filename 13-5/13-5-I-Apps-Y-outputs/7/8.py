
def get_input():
    return list(map(int, input().split()))

def solve(X, Y, Z):
    return (X - Z) // (Y + Z)

def main():
    X, Y, Z = get_input()
    print(solve(X, Y, Z))

if __name__ == '__main__':
    main()

