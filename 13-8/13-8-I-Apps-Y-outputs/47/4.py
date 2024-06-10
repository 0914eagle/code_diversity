
def calculate_expected_score(n, k):
    # Calculate the probability of each outcome
    probabilities = [1 / n] * n

    # Calculate the expected score for each outcome
    expected_scores = [i * probabilities[i - 1] for i in range(1, n + 1)]

    # Calculate the expected score after k rounds
    expected_score = 0
    for i in range(k):
        expected_score += expected_scores[i]

    return expected_score

def main():
    n, k = map(int, input().split())
    print(calculate_expected_score(n, k))

if __name__ == '__main__':
    main()

