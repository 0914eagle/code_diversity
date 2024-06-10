
def count_permutations(n, x, pos):
    MOD = 10**9 + 7
    
    def calculate_combinations(n, r):
        if r > n:
            return 0
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator = (numerator * (n - i)) % MOD
            denominator = (denominator * (i + 1)) % MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
    
    left_count = pos
    right_count = n - pos - 1
    smaller_count = x - 1
    larger_count = n - x
    
    result = (calculate_combinations(smaller_count + larger_count, smaller_count) * calculate_combinations(left_count + right_count, left_count)) % MOD
    result = (result * calculate_combinations(n - 1, left_count)) % MOD
    
    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_permutations(n, x, pos))
