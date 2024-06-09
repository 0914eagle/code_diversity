
def solve(n, buttons):
    # Initialize a list to store the answers
    answers = []
    
    # Loop through each possible combination of buttons
    for combination in itertools.permutations(range(n)):
        # Check if the current combination is valid
        if is_valid_combination(combination, buttons):
            # If it is valid, add it to the list of answers
            answers.append(combination)
    
    # Return the list of answers
    return answers

def is_valid_combination(combination, buttons):
    # Initialize a set to store the buttons that have been used
    used_buttons = set()
    
    # Loop through each person in the combination
    for person in combination:
        # Check if the current button has already been used
        if person in used_buttons:
            # If it has, return False
            return False
        # Add the current button to the set of used buttons
        used_buttons.add(person)
    
    # If we reach this point, all buttons have been used and no button has been used more than once, so return True
    return True

