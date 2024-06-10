
def count_permutations(n, x, pos):
    MOD = 10**9 + 7

    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result = (result * i) % MOD
        return result

    def nCr(n, r):
        numerator = factorial(n)
        denominator = (factorial(r) * factorial(n - r)) % MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD

    left_count = pos
    right_count = n - pos - 1
    smaller_count = x - 1
    larger_count = n - x

    result = (nCr(left_count + right_count, left_count) * nCr(smaller_count + larger_count, smaller_count)) % MOD
    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_permutations(n, x, pos))
