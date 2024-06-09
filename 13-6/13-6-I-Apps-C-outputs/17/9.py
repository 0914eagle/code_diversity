
def solve(n, crush):
    # Initialize a dictionary to store the number of rounds required for each person to become the Joon-Joon
    rounds = {}
    for i in range(n):
        # If a person's crush is themselves, they require 1 round to become the Joon-Joon
        if crush[i] == i:
            rounds[i] = 1
        # Otherwise, they require 2 rounds to become the Joon-Joon
        else:
            rounds[i] = 2
    
    # Iterate through the dictionary and find the minimum number of rounds required for all persons to become the Joon-Joon
    min_rounds = min(rounds.values())
    
    # If the minimum number of rounds is 1, return 1, otherwise return -1
    if min_rounds == 1:
        return 1
    else:
        return -1

