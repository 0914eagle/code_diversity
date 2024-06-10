
from itertools import permutations

MOD = 10**9 + 7

def calculate_factorials(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append((factorials[-1] * i) % MOD)
    return factorials

def generate_composite_strings(initial_strings, k):
    composites = set()
    for perm in permutations(initial_strings, k):
        composites.add(''.join(perm))
    return sorted(composites)

def find_position(composite_strings, test_string):
    return composite_strings.index(test_string) + 1

if __name__ == "__main__":
    n, k = map(int, input().split())
    initial_strings = [input().strip() for _ in range(n)]
    test_string = input().strip()

    factorials = calculate_factorials(n)
    composite_strings = generate_composite_strings(initial_strings, k)
    position = find_position(composite_strings, test_string)

    prefix_sums = sum(factorials[i] for i in range(k))
    position = (position + prefix_sums) % MOD

    print(position)
