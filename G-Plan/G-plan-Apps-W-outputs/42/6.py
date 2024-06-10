
import math

def can_fit_in_deadline(n, d):
    x = math.isqrt(d) - 1
    total_days = x + math.ceil(d / (x + 1))
    return "YES" if total_days <= n else "NO"

def solve_test_cases(test_cases):
    results = []
    for n, d in test_cases:
        results.append(can_fit_in_deadline(n, d))
    return results

if __name__ == '__main__':
    T = int(input())
    test_cases = [tuple(map(int, input().split())) for _ in range(T)]
    results = solve_test_cases(test_cases)
    for result in results:
        print(result)
