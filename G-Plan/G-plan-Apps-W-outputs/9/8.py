
def is_divisible_by_p(coeff, p):
    return coeff % p == 0

def find_non_divisible_power(n, m, p, a_coeffs, b_coeffs):
    for t in range(n + m - 1):
        coeff = 0
        for i in range(n):
            for j in range(m):
                if i + j == t:
                    coeff += a_coeffs[i] * b_coeffs[j]
        if not is_divisible_by_p(coeff, p):
            return t

if __name__ == "__main__":
    n, m, p = map(int, input().split())
    a_coeffs = list(map(int, input().split()))
    b_coeffs = list(map(int, input().split()))
    
    result = find_non_divisible_power(n, m, p, a_coeffs, b_coeffs)
    print(result)
