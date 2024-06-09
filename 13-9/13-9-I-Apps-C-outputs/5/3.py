
import re

def solve(n, s, predictions):
    # Initialize an array to store the probability of each prediction
    probabilities = [0] * s

    # Iterate over each prediction
    for i in range(s):
        # Get the length of the prediction
        length = len(predictions[i])

        # Initialize a counter to count the number of occurrences of each symbol
        count = [0] * 3

        # Iterate over each symbol in the prediction
        for j in range(length):
            # Get the symbol at the current position
            symbol = predictions[i][j]

            # Increment the count for the current symbol
            count[symbols.index(symbol)] += 1

        # Calculate the probability of each symbol in the prediction
        probabilities[i] = (count[0] / length) * (count[1] / length) * (count[2] / length)

    # Sort the predictions by probability in descending order
    sorted_predictions = sorted(range(s), key=lambda i: probabilities[i], reverse=True)

    # Return the sorted predictions
    return [predictions[i] for i in sorted_predictions]

if __name__ == '__main__':
    n, s = map(int, input().split())
    predictions = [input() for _ in range(s)]
    print(*solve(n, s, predictions), sep='\n')

