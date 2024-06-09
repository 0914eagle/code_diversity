
def solve(barbarians, rounds):
    # Initialize a dictionary to store the number of consecutive substrings for each barbarian
    consecutive_substrings = {}
    for i in range(len(barbarians)):
        consecutive_substrings[i+1] = 0
    
    # Iterate through the rounds
    for round in rounds:
        if round[0] == 1:
            # If the round is of type 1, increment the number of consecutive substrings for each barbarian
            word = round[1]
            for i in range(len(barbarians)):
                if word in barbarians[i]:
                    consecutive_substrings[i+1] += 1
        else:
            # If the round is of type 2, return the number of consecutive substrings for the specified barbarian
            barbarian = round[1]
            return consecutive_substrings[barbarian]

