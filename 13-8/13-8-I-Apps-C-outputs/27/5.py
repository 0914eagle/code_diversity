
def solve(barbarians, rounds):
    # Initialize a dictionary to store the number of consecutive substrings for each barbarian
    num_consecutive_substrings = {}
    for i in range(len(barbarians)):
        num_consecutive_substrings[i+1] = 0
    
    # Iterate through the rounds
    for round in rounds:
        # If the round is of type 1, update the number of consecutive substrings for each barbarian
        if round[0] == 1:
            word = round[1]
            for i in range(len(barbarians)):
                if word in barbarians[i]:
                    num_consecutive_substrings[i+1] += 1
        # If the round is of type 2, output the number of consecutive substrings for the specified barbarian
        elif round[0] == 2:
            barbarian = round[1]
            print(num_consecutive_substrings[barbarian])

