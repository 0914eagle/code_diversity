
def maximize_value(n, k, a):
    b = [0] * n
    remaining_space = k
    for i in range(n):
        b[i] = min(a[i], remaining_space)
        remaining_space -= b[i]
    return b

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = maximize_value(n, k, a)
print(*result)
