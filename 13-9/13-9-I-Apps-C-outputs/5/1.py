
import collections

def solve(n, s, predictions):
    # Initialize a dictionary to store the counts of each prediction
    prediction_counts = collections.defaultdict(int)

    # Iterate over each prediction
    for prediction in predictions:
        # Get the length of the prediction
        length = len(prediction)

        # Iterate over each character in the prediction
        for i in range(length):
            # Get the current character
            char = prediction[i]

            # Get the substring starting from the current character and ending at the end of the prediction
            substring = prediction[i:]

            # Increment the count of the substring
            prediction_counts[substring] += 1

    # Sort the predictions by decreasing count
    sorted_predictions = sorted(prediction_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted predictions
    return sorted_predictions

