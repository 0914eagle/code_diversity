
def get_largest_integer(A, B, X):
    for i in range(10**9):
        if A*i + B*len(str(i)) <= X:
            return i
    return 0

if __name__ == '__main__':
    A, B, X = map(int, input().split())
    print(get_largest_integer(A, B, X))

