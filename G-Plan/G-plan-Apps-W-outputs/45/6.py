
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

    left_count = x - 1
    right_count = n - x
    left_positions = pos
    right_positions = n - pos - 1

    result = (nCr(left_count, left_positions) * nCr(right_count, right_positions)) % MOD
    result = (result * factorial(left_count)) % MOD
    result = (result * factorial(right_count)) % MOD

    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_permutations(n, x, pos))
