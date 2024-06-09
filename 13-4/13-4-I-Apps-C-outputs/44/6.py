
def get_maximum_number_of_times(n, buttons):
    # Initialize a list to store the results
    results = []
    
    # Loop through each possible combination of buttons
    for combination in itertools.permutations(range(1, n+1)):
        # Check if the current combination is valid
        if is_valid_combination(combination, buttons):
            # If the current combination is valid, add it to the results list
            results.append(list(combination))
    
    # Return the maximum number of times and the corresponding results
    return len(results), results

def is_valid_combination(combination, buttons):
    # Initialize a set to store the buttons that have been used
    used_buttons = set()
    
    # Loop through each person in the combination
    for person in combination:
        # Check if the current person's button has already been used
        if person in used_buttons:
            # If the current person's button has already been used, return False
            return False
        # Add the current person's button to the used buttons set
        used_buttons.add(person)
    
    # If all buttons have been used and no button has been used more than once, return True
    return len(used_buttons) == len(buttons)

# Test the function with the sample input
n = 3
buttons = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]
maximum_number_of_times, results = get_maximum_number_of_times(n, buttons)
print(maximum_number_of_times)
print(results)

