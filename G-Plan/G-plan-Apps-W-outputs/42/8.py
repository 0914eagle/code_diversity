fit_deadline(n, d):
    x = int((d ** 0.5) - 1)
    total_days = x + ((d // (x + 1)) if d % (x + 1) == 0 else (d // (x + 1)) + 1)
    return "YES" if total_days <= n else "NO"

def solve_test_cases(test_cases):
    results = []
    for n, d in test_cases:
        results.append(can_fit_deadline(n, d))
    return results

if __name__ == '__main__':
    T = int(input())
    test_cases = [tuple(map(int, input().split())) for _ in range(T)]
    results = solve_test_cases(test_cases)
    for result in results:
        print(result)
