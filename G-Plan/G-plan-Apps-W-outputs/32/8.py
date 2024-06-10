
def calculate_xor_sum(u, v):
    if u > v or (v - u) % 2 != 0:
        return -1, []

    n = (v - u) // 2
    if u == 0:
        return n, [1] * n
    else:
        return n + 1, [u] + [1] * (n - 1)

if __name__ == "__main__":
    u, v = map(int, input().split())
    length, array = calculate_xor_sum(u, v)
    print(length)
    print(*array)
