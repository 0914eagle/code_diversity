
def solve(barbarians, rounds):
    # Initialize a dictionary to store the count of consecutive substrings for each barbarian
    barbarian_counts = {}
    for i, word in enumerate(barbarians, start=1):
        barbarian_counts[i] = 0
    
    # Iterate through the rounds
    for round in rounds:
        if round[0] == 1:
            # If the round is of the first type, show the word to all the barbarians
            for barbarian in barbarian_counts:
                if round[1] in barbarians[barbarian-1]:
                    barbarian_counts[barbarian] += 1
        else:
            # If the round is of the second type, ask the question to the barbarian
            barbarian = round[1]
            count = 0
            for word in barbarians:
                if round[1] in word:
                    count += 1
            print(count)
    return barbarian_counts

