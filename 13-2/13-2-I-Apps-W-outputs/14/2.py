
def find_pair(n):
    for a in range(1, n):
        b = (n - 3**a) // 5
        if 3**a + 5**b == n:
            return a, b
    return -1, -1

