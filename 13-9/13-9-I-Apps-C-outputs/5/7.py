
import collections

def get_sorted_predictions(n, s, predictions):
    # Initialize a dictionary to store the frequency of each prediction
    prediction_freq = collections.defaultdict(int)

    # Loop through each prediction and increment the frequency of each prediction
    for prediction in predictions:
        prediction_freq[prediction] += 1

    # Sort the predictions by frequency in descending order
    sorted_predictions = sorted(prediction_freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_predictions

