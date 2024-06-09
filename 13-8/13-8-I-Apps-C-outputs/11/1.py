
def solve(n, s, predictions):
    # Initialize an empty list to store the sorted predictions
    sorted_predictions = []

    # Loop through each prediction
    for prediction in predictions:
        # Calculate the probability of the prediction appearing sometime during the final match
        probability = 1
        for i in range(len(prediction)):
            if prediction[i] == "R":
                probability *= 1/3
            elif prediction[i] == "P":
                probability *= 1/3
            elif prediction[i] == "S":
                probability *= 1/3

        # Add the prediction to the sorted list with its probability
        sorted_predictions.append([prediction, probability])

    # Sort the list by probability in descending order
    sorted_predictions.sort(key=lambda x: x[1], reverse=True)

    # Return the sorted predictions
    return [prediction for prediction, probability in sorted_predictions]

