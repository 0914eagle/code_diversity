
def find_non_divisible_power(n, m, p, coefficients_f, coefficients_g):
    for t in range(n + m - 1):
        coefficient_t = 0
        for i in range(n):
            for j in range(m):
                if i + j == t:
                    coefficient_t += coefficients_f[i] * coefficients_g[j]
        if coefficient_t % p != 0:
            return t

if __name__ == "__main__":
    n, m, p = map(int, input().split())
    coefficients_f = list(map(int, input().split()))
    coefficients_g = list(map(int, input().split()))
    print(find_non_divisible_power(n, m, p, coefficients_f, coefficients_g))
