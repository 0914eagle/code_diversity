
from itertools import permutations

MOD = 10**9 + 7

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def calculate_position(n, k, initial_strings, test_string):
    initial_strings = sorted(initial_strings)
    perms = permutations(initial_strings, k)
    all_composites = [''.join(p) for p in perms]
    all_composites.sort()

    position = all_composites.index(test_string) + 1
    return position % MOD

if __name__ == "__main__":
    n, k = map(int, input().split())
    initial_strings = [input().strip() for _ in range(n)]
    test_string = input().strip()
    
    result = calculate_position(n, k, initial_strings, test_string)
    print(result)
