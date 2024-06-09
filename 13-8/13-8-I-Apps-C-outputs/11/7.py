
def rock_paper_scissors(n, s):
    # Initialize an empty list to store the predictions
    predictions = []

    # Iterate over the input sequences
    for _ in range(s):
        # Read a sequence of length n
        sequence = input()

        # Calculate the probability of the sequence occurring
        probability = 1
        for i in range(1, len(sequence)):
            if sequence[i] == "R":
                probability *= 1/3
            elif sequence[i] == "P":
                probability *= 1/3
            else:
                probability *= 1/3

        # Add the sequence and its probability to the list
        predictions.append((sequence, probability))

    # Sort the list by probability in descending order
    predictions.sort(key=lambda x: x[1], reverse=True)

    # Return the sorted list of predictions
    return predictions

