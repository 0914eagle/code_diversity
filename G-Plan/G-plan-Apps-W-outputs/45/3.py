
def count_valid_permutations(n, x, pos):
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

    left_count = x - 1
    right_count = n - x
    remaining_count = n - 1 - left_count - right_count

    ways_to_place_left = binomial_coefficient(pos, left_count)
    ways_to_place_right = binomial_coefficient(remaining_count, right_count)

    total_permutations = (ways_to_place_left * ways_to_place_right) % MOD
    return (total_permutations * factorial(remaining_count)) % MOD

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    result = count_valid_permutations(n, x, pos)
    print(result)
