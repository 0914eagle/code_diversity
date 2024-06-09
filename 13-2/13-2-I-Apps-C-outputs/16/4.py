
def find_square_root(n):
    for i in range(1, n+1):
        if i*i == n:
            return i
    return -1

