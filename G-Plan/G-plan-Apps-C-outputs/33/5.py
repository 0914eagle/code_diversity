
from itertools import permutations

MOD = 10**9 + 7

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

def calculate_position(n, k, initial_strings, test_string):
    all_composite_strings = [''.join(p) for p in permutations(initial_strings, k)]
    all_composite_strings.sort()
    
    position = all_composite_strings.index(test_string) + 1
    return position % MOD

if __name__ == "__main__":
    n, k = map(int, input().split())
    initial_strings = [input().strip() for _ in range(n)]
    test_string = input().strip()
    
    result = calculate_position(n, k, initial_strings, test_string)
    print(result)
