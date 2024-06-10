
def count_permutations(n, x, pos):
    MOD = 10**9 + 7

    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % MOD
        return result

    def binomial_coefficient(n, k):
        numerator = factorial(n)
        denominator = (factorial(k) * factorial(n - k)) % MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD

    smaller_count = pos
    larger_count = n - pos - 1

    result = (binomial_coefficient(smaller_count + larger_count, smaller_count) * factorial(smaller_count) * factorial(larger_count)) % MOD

    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_permutations(n, x, pos))
