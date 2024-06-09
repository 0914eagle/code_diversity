
def f1(n, s, predictions):
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

    return [predictions[i] for i in sorted_predictions]

def f2(n, s, predictions):
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

    return [predictions[i] for i in sorted_predictions]

if __name__ == '__main__':
    n = int(input())
    s = int(input())
    predictions = []
    for i in range(s):
        predictions.append(input())
    print(f1(n, s, predictions))
    print(f2(n, s, predictions))

