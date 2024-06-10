
def count_valid_permutations(n, x, pos):
    MOD = 10**9 + 7

    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result = (result * i) % MOD
        return result

    def nCr(n, r):
        return (factorial(n) // (factorial(r) * factorial(n - r))) % MOD

    smaller_count = pos
    larger_count = n - pos - 1
    remaining_count = n - 1 - smaller_count - larger_count

    result = (nCr(smaller_count, smaller_count) * nCr(larger_count, larger_count) * factorial(remaining_count)) % MOD

    return result

if __name__ == '__main__':
    n, x, pos = map(int, input().split())
    print(count_valid_permutations(n, x, pos))
