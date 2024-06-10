
from itertools import permutations

MOD = 10**9 + 7

def calculate_factorial(n):
    factorial = [1]
    for i in range(1, n + 1):
        factorial.append((factorial[-1] * i) % MOD)
    return factorial

def generate_composite_strings(initial_strings, k):
    composites = set()
    for perm in permutations(initial_strings, k):
        composites.add(''.join(perm))
    return sorted(composites)

def binary_search(composite_strings, test_string):
    left, right = 0, len(composite_strings) - 1
    while left <= right:
        mid = (left + right) // 2
        if composite_strings[mid] == test_string:
            return mid + 1
        elif composite_strings[mid] < test_string:
            left = mid + 1
        else:
            right = mid - 1

def main():
    n, k = map(int, input().split())
    initial_strings = [input().strip() for _ in range(n)]
    test_string = input().strip()

    factorial = calculate_factorial(n)
    composite_strings = generate_composite_strings(initial_strings, k)
    position = binary_search(composite_strings, test_string)

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = (prefix_sum[i - 1] + factorial[i - 1]) % MOD

    result = (prefix_sum[n] * (position - 1)) % MOD
    print(result)

if __name__ == "__main__":
    main()
