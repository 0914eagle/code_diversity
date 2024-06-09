
import itertools

def get_probability(prediction, n):
    # Initialize a list to store the probability of each prediction
    probabilities = [0] * len(prediction)

    # Iterate over all possible combinations of the prediction
    for combination in itertools.permutations(prediction):
        # Check if the combination is a contiguous sequence of the prediction
        if all(combination[i] == prediction[i % len(prediction)] for i in range(len(combination))):
            # If it is, add the probability of the combination to the list
            probabilities[len(combination) - 1] += 1

    # Return the list of probabilities, normalized by the total number of combinations
    return [prob / math.factorial(len(prediction)) for prob in probabilities]

def get_sorted_predictions(predictions, n):
    # Initialize an empty list to store the sorted predictions
    sorted_predictions = []

    # Iterate over all predictions
    for prediction in predictions:
        # Get the probability of the prediction
        probability = get_probability(prediction, n)

        # Add the prediction and its probability to the sorted list
        sorted_predictions.append((prediction, probability))

    # Sort the list by probability, in descending order
    sorted_predictions.sort(key=lambda x: x[1], reverse=True)

    # Return the sorted list of predictions
    return sorted_predictions

def main():
    # Read the input
    n, s = map(int, input().split())
    predictions = [input() for _ in range(s)]

    # Get the sorted predictions
    sorted_predictions = get_sorted_predictions(predictions, n)

    # Print the sorted predictions
    for prediction, probability in sorted_predictions:
        print(prediction)

if __name__ == "__main__":
    main()

