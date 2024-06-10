
def get_largest_integer(A, B, X):
    for i in range(1, 10**9):
        if A*i + B*len(str(i)) <= X:
            return i
    return 0

def main():
    A, B, X = map(int, input().split())
    print(get_largest_integer(A, B, X))

if __name__ == '__main__':
    main()

