
def get_expected_score(n, k):
    
    # Initialize the probability of each outcome
    probabilities = [1 / n] * n

    # Loop through each roll
    for i in range(k):
        # Calculate the probability of each outcome after this roll
        new_probabilities = [0] * n
        for j in range(n):
            # Calculate the probability of each outcome given this roll
            given_probabilities = [probabilities[j] / n] * n
            # Calculate the probability of each outcome after this roll
            for k in range(n):
                new_probabilities[k] += given_probabilities[j]
        # Update the probabilities
        probabilities = new_probabilities

    # Calculate the expected score
    expected_score = 0
    for i in range(n):
        expected_score += i * probabilities[i]

    return expected_score

def main():
    # Read the input
    n, k = map(int, input().split())

    # Calculate the expected score
    expected_score = get_expected_score(n, k)

    # Print the output
    print(expected_score)

if __name__ == '__main__':
    main()

