
def calculate_max_score(n, m, scores):
    total_sum = sum(scores)
    max_score = min(scores[0] + m - total_sum, m)
    return max_score

def process_test_cases(test_cases):
    results = []
    for test in test_cases:
        n, m = test[0], test[1]
        scores = test[2]
        max_score = calculate_max_score(n, m, scores)
        results.append(max_score)
    return results

if __name__ == "__main__":
    t = int(input())
    test_cases = []
    for _ in range(t):
        n, m = map(int, input().split())
        scores = list(map(int, input().split()))
        test_cases.append((n, m, scores))
    
    results = process_test_cases(test_cases)
    for result in results:
        print(result)
