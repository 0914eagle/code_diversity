
def solve(barbarians, rounds):
    # Initialize a dictionary to store the count of consecutive substrings for each barbarian
    counts = {barbarian: 0 for barbarian in barbarians}

    # Iterate over the rounds
    for round in rounds:
        # If the round is of type 1, update the count for the corresponding barbarian
        if round[0] == 1:
            counts[round[1]] += 1
        # If the round is of type 2, output the count for the corresponding barbarian
        else:
            print(counts[round[1]])

    return counts

