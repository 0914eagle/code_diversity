
import sys

def solve(n, s, predictions):
    # Convert the predictions to integers (0 for Rock, 1 for Paper, 2 for Scissors)
    predictions = [ord(p) - ord('R') for p in predictions]
    
    # Calculate the number of possible outcomes for each prediction
    num_outcomes = [0] * s
    for i in range(s):
        num_outcomes[i] = n - len(predictions[i]) + 1
    
    # Calculate the likelihood of each prediction appearing sometime during the match
    likelihood = [0] * s
    for i in range(s):
        likelihood[i] = 1
        for j in range(s):
            if i != j:
                likelihood[i] *= num_outcomes[j] / n
    
    # Sort the predictions by decreasing likelihood
    sorted_predictions = sorted(range(s), key=lambda i: -likelihood[i])
    
    return [predictions[i] for i in sorted_predictions]

if __name__ == '__main__':
    n, s = map(int, input().split())
    predictions = [input() for _ in range(s)]
    print(*solve(n, s, predictions), sep='\n')

