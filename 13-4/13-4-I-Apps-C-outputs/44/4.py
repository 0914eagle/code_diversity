
def get_max_people_on_buttons(n, buttons):
    # Initialize a list to store the results
    results = []
    
    # Iterate over each possible combination of people on the buttons
    for combination in itertools.permutations(range(1, n + 1)):
        # Check if the current combination is valid
        if is_valid_combination(combination, buttons):
            # If the combination is valid, add it to the results list
            results.append(list(combination))
    
    # Return the maximum number of people on the buttons and the corresponding results
    return len(results), results

def is_valid_combination(combination, buttons):
    # Initialize a set to store the buttons that have been occupied
    occupied_buttons = set()
    
    # Iterate over each person in the combination
    for person in combination:
        # Check if the person's button has already been occupied
        if person in occupied_buttons:
            # If the button has already been occupied, return False
            return False
        # Add the person's button to the occupied buttons set
        occupied_buttons.add(person)
    
    # If all the buttons have been occupied and no button has been occupied more than once, return True
    return len(occupied_buttons) == len(buttons)

# Test the function with the sample input
n = 3
buttons = ["YYY", "NYY", "YNY"]
max_people, results = get_max_people_on_buttons(n, buttons)
print(max_people)
print(*results, sep="\n")

