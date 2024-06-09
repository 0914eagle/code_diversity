
def solve(n, s, predictions):
    # Initialize an array to store the probability of each prediction
    probabilities = [0] * s

    # Loop through each prediction and calculate its probability
    for i in range(s):
        prediction = predictions[i]
        probability = 1
        for j in range(len(prediction)):
            if prediction[j] == "R":
                probability *= 1/3
            elif prediction[j] == "P":
                probability *= 1/3
            else:
                probability *= 1/3
        probabilities[i] = probability

    # Sort the predictions by probability in descending order
    sorted_predictions = sorted(range(s), key=lambda i: probabilities[i], reverse=True)

    # Return the sorted predictions
    return [predictions[i] for i in sorted_predictions]

