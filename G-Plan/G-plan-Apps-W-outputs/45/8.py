
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
    
    smaller_count = pos
    larger_count = n - pos - 1
    
    result = (nCr(smaller_count, x - 1) * nCr(larger_count, n - x)) % MOD
    result = (result * factorial(smaller_count)) % MOD
    result = (result * factorial(larger_count)) % MOD
    result = (result * factorial(n - 1 - smaller_count - larger_count)) % MOD
    
    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_permutations(n, x, pos))
