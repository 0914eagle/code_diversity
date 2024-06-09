
def solve(n, p, m, participants, scores):
    # Initialize a dictionary to store the names and scores of the participants
    participant_scores = {}

    # Iterate over the list of participants and their scores
    for i in range(m):
        # Extract the name and score of the current participant
        name, score = participants[i], scores[i]

        # If the participant is not in the dictionary, add them with their score
        if name not in participant_scores:
            participant_scores[name] = score
        # If the participant is already in the dictionary, add their score to the current total
        else:
            participant_scores[name] += score

    # Find the participants who reached the minimum required score
    winners = [name for name, score in participant_scores.items() if score >= p]

    # If no one reached the minimum required score, return "No winner!"
    if not winners:
        return "No winner!"

    # Return the names of the winners, separated by newlines
    return "\n".join(winners) + " wins!"

