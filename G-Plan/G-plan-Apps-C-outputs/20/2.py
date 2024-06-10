
from itertools import combinations
from sympy import factorint

def calculate_prime_factors_sum(data_pieces, combination):
    prime_factors_sum = 0
    for idx, val in enumerate(combination):
        prime_factors_sum += sum(factorint(data_pieces[val]).values())
    return prime_factors_sum

def max_revenue(data_pieces):
    n = len(data_pieces)
    max_rev = 0
    for i in range(1, n + 1):
        for comb in combinations(range(n), i):
            prime_factors_sum = calculate_prime_factors_sum(data_pieces, comb)
            max_rev = max(max_rev, prime_factors_sum)
    return max_rev

if __name__ == "__main__":
    N = int(input())
    data_pieces = list(map(int, input().split()))
    print(max_revenue(data_pieces))
