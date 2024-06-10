
def calculate_max_score(n, m, scores):
    total_sum = sum(scores)
    max_score = min(scores[0] + m - total_sum, m)
    return max_score

def process_test_case():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        scores = list(map(int, input().split()))
        result = calculate_max_score(n, m, scores)
        print(result)

if __name__ == "__main__":
    process_test_case()
