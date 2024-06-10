
def calculate_xor_sum(u, v):
    if u > v or (u - v) % 2 != 0:
        return -1

    n = (u + v) // 2
    if n == 0:
        return 0

    result = [0] * n
    for i in range(60):
        if u & (1 << i):
            result[i] = 1

    xor_val = 0
    for i in range(n):
        xor_val ^= result[i]

    if xor_val == u:
        return n, result
    else:
        return -1


if __name__ == "__main__":
    u, v = map(int, input().split())
    res = calculate_xor_sum(u, v)
    if res == -1:
        print(-1)
    else:
        n, arr = res
        print(n)
        print(*arr)
