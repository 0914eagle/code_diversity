
from itertools import permutations

MOD = 10**9 + 7

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % MOD
    return result

def calculate_positions(n, k):
    positions = [0] * (n+1)
    positions[0] = 1
    for i in range(1, n+1):
        positions[i] = (positions[i-1] * i) % MOD
    return positions

def find_position(sorted_composites, test_string):
    return sorted_composites.index(test_string) + 1

def generate_composite_strings(initial_strings, k):
    composites = set()
    for perm in permutations(initial_strings, k):
        composites.add(''.join(perm))
    return sorted(composites)

if __name__ == "__main__":
    n, k = map(int, input().split())
    initial_strings = [input().strip() for _ in range(n)]
    test_string = input().strip()
    
    sorted_composites = generate_composite_strings(initial_strings, k)
    positions = calculate_positions(n, k)
    
    test_position = find_position(sorted_composites, test_string)
    print(positions[n] * (sorted_composites.index(test_string) + 1) % MOD)
