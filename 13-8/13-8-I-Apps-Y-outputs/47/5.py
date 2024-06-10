
def expected_score(n, k):
    # Initialize the probability of each outcome
    probabilities = [1 / n] * n

    # Initialize the expected score for each outcome
    expected_scores = [i for i in range(1, n + 1)]

    # Loop through each roll
    for i in range(k):
        # Calculate the probability of each outcome after this roll
        probabilities = [j / n for j in range(1, n + 1)]

        # Calculate the expected score for each outcome after this roll
        expected_scores = [sum(probabilities[j] * j for j in range(i, n + 1)) for i in range(n)]

    # Return the expected score for the final roll
    return expected_scores[n - 1]

def main():
    n, k = map(int, input().split())
    print(expected_score(n, k))

if __name__ == '__main__':
    main()

