
def calculate_xor_sum(u, v):
    if u == 0 and v == 0:
        return [0]
    if u == 0 or u > v or (v - u) % 2 != 0:
        return [-1]

    n = 1
    while n * n <= v:
        if (v - u) % n == 0:
            a = (v - u) // n
            x = (a + n) // 2
            y = (a - n) // 2
            if x ^ y == u:
                return [x] * n + [y] * n
        n += 1

    return [-1]

if __name__ == "__main__":
    u, v = map(int, input().split())
    result = calculate_xor_sum(u, v)
    if result[0] == -1:
        print(-1)
    else:
        print(len(result))
        print(*result)
