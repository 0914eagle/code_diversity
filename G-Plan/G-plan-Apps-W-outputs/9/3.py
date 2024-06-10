
def is_divisible_by_p(coeff, p):
    return coeff % p == 0

def find_power_not_divisible(n, m, p, a, b):
    for t in range(n + m - 1):
        coeff = 0
        for i in range(n):
            for j in range(m):
                if i + j == t:
                    coeff += a[i] * b[j]
        if not is_divisible_by_p(coeff, p):
            return t

if __name__ == "__main__":
    n, m, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(find_power_not_divisible(n, m, p, a, b))
