
def get_largest_integer(A, B, X):
    for i in range(10**9):
        if A*i + B*len(str(i)) <= X:
            return i
    return 0

