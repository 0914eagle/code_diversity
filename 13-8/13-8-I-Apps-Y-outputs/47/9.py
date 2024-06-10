
def calculate_expected_score(n, k):
    # Initialize the probability distribution
    probability_distribution = [1 / n] * n

    # Calculate the expected score for each possible roll
    expected_score = [0] * n
    for i in range(n):
        expected_score[i] = i + 1

    # Calculate the expected score for each possible roll with k-1 rerolls
    for i in range(n):
        for j in range(k-1):
            expected_score[i] += probability_distribution[i] * (j+1)

    # Calculate the expected score for each possible roll with k rerolls
    for i in range(n):
        expected_score[i] += probability_distribution[i] * k

    # Return the maximum expected score
    return max(expected_score)

def main():
    n, k = map(int, input().split())
    print(calculate_expected_score(n, k))

if __name__ == '__main__':
    main()

