
def calculate_xor_sum(u, v):
    if u > v or (u - v) % 2 != 0:
        return -1, []
    
    n = (v - u) // 2
    if u == 0:
        return n, [1] * n
    elif n & u:
        return 3, [n, u, u]
    else:
        return 2, [n + u, n]

if __name__ == "__main__":
    u, v = map(int, input().split())
    length, arr = calculate_xor_sum(u, v)
    print(length)
    if length > 0:
        print(*arr)
