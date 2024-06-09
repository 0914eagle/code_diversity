
def get_largest_integer(A, B, X):
    for i in range(1, 10**9+1):
        if A*i + B*len(str(i)) <= X:
            return i
    return 0

