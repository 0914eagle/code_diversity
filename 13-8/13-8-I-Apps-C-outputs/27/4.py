
def solve(barbarians, questions):
    # Initialize a dictionary to store the number of consecutive substrings for each barbarian
    consecutive_substrings = {barbarian: 0 for barbarian in barbarians}

    # Iterate over each question
    for question in questions:
        # If the question is of the first type, update the dictionary with the number of consecutive substrings for each barbarian
        if question[0] == 1:
            word = question[1]
            for barbarian in barbarians:
                if word in barbarian:
                    consecutive_substrings[barbarian] += 1
        # If the question is of the second type, return the number of consecutive substrings for the specified barbarian
        else:
            barbarian = question[1]
            return consecutive_substrings[barbarian]


