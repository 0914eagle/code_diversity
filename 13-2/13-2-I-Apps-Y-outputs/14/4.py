
def solve(n, p, m, names, scores):
    # Initialize a dictionary to store the names and scores
    name_scores = {}

    # Iterate over the list of names and scores
    for i in range(len(names)):
        # Check if the current name is already in the dictionary
        if names[i] in name_scores:
            # If it is, add the current score to the total score
            name_scores[names[i]] += scores[i]
        else:
            # If it's not, add the current name and score to the dictionary
            name_scores[names[i]] = scores[i]

    # Initialize a list to store the winners
    winners = []

    # Iterate over the dictionary
    for name, score in name_scores.items():
        # Check if the current score is greater than or equal to the minimum required score
        if score >= p:
            # If it is, add the current name to the list of winners
            winners.append(name)

    # If no one reached the minimum required score, return "No winner!"
    if not winners:
        return "No winner!"

    # Otherwise, return the names of the winners, separated by newlines
    return "\n".join(winners) + " wins!"

