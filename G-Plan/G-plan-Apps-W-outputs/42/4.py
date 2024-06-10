mize_program(n, d):
    return (d <= n)

def can_fit_within_deadline(T, test_cases):
    results = []
    for i in range(T):
        n, d = test_cases[i]
        if optimize_program(n, d):
            results.append("YES")
        else:
            results.append("NO")
    return results

if __name__ == '__main__':
    T = int(input())
    test_cases = []
    for _ in range(T):
        n, d = map(int, input().split())
        test_cases.append((n, d))
    
    results = can_fit_within_deadline(T, test_cases)
    for result in results:
        print(result)
