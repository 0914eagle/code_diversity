
def find_pair(n):
    for a in range(1, n):
        for b in range(1, n):
            if 3**a + 5**b == n:
                return a, b
    return -1, -1

