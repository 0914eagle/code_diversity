
def is_pair_exists(n):
    for a in range(1, n):
        b = (n - 3**a) // 5
        if 3**a + 5**b == n:
            return True, a, b
    return False, -1, -1

n = int(input())
exists, a, b = is_pair_exists(n)
if exists:
    print(a, b)
else:
    print(-1)

