
def solve(k, n, questions):
    # Initialize a list to store the player labels
    labels = list(range(1, 9))
    # Remove the player with the box from the list
    labels.remove(k)
    # Iterate through the questions
    for i in range(n):
        # Get the time and answer type for the current question
        time, answer = questions[i]
        # If the answer is correct, pass the box to the next player
        if answer == "T":
            k = labels[labels.index(k) - 1]
        # If the answer is incorrect or skipped, pass the box to the next player
        else:
            k = labels[labels.index(k) - 2]
    # Return the player label with the box when it exploded
    return k

