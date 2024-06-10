
def count_valid_permutations(n, x, pos):
    mod = 10**9 + 7

    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result = (result * i) % mod
        return result

    def calculate_combinations(n, r):
        numerator = factorial(n)
        denominator = (factorial(r) * factorial(n - r)) % mod
        return (numerator * pow(denominator, mod - 2, mod)) % mod

    left_count = pos
    right_count = n - pos - 1
    smaller_count = x - 1
    larger_count = n - x

    result = (calculate_combinations(left_count + right_count, left_count) * calculate_combinations(smaller_count + larger_count, smaller_count)) % mod
    result = (result * factorial(left_count) * factorial(right_count) * factorial(smaller_count) * factorial(larger_count)) % mod

    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_valid_permutations(n, x, pos))
