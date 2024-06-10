
import math

def expected_score(n, k):
    # Calculate the probability of each outcome
    probabilities = [1 / n] * n

    # Calculate the expected score for each outcome
    expected_scores = [i * probabilities[i - 1] for i in range(1, n + 1)]

    # Calculate the total expected score
    total_expected_score = sum(expected_scores)

    # Return the total expected score
    return total_expected_score

def main():
    n, k = map(int, input().split())
    print(expected_score(n, k))

if __name__ == '__main__':
    main()

