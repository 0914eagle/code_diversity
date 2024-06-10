
def find_non_divisible_power(n, m, p, a, b):
    for t in range(n + m - 1):
        c_t = 0
        for i in range(n):
            for j in range(m):
                if i + j == t:
                    c_t += a[i] * b[j]
        if c_t % p != 0:
            return t

if __name__ == "__main__":
    n, m, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(find_non_divisible_power(n, m, p, a, b))
