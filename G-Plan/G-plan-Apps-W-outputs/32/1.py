
def calculate_xor_sum(u, v):
    if u > v or (u - v) % 2 != 0:
        return -1

    n = (u - v) // 2
    if n == 0:
        return 0

    res = [n]
    if n & v == 0:
        res.append(n + v)
    return res

if __name__ == "__main__":
    u, v = map(int, input().split())
    result = calculate_xor_sum(u, v)
    if result == -1:
        print(-1)
    else:
        print(len(result))
        print(*result)
