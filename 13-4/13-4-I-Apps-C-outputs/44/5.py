
def get_max_times(n, buttons):
    # Initialize a list to store the results
    results = []
    
    # Loop through each possible combination of buttons
    for combination in itertools.permutations(range(1, n+1)):
        # Check if the current combination is valid
        if is_valid_combination(combination, buttons):
            # If it is valid, add it to the results list
            results.append(list(combination))
    
    # Return the maximum number of times and the corresponding combinations
    return len(results), results

def is_valid_combination(combination, buttons):
    # Check if the current combination is valid by checking if no person stands on the same button more than once
    for i in range(len(combination)):
        for j in range(i+1, len(combination)):
            if combination[i] == combination[j]:
                return False
    
    # Check if the current combination is valid by checking if no person stands on a button that is already occupied by another person
    for i in range(len(combination)):
        for j in range(i+1, len(combination)):
            if buttons[combination[i]-1][combination[j]-1] == 'N':
                return False
    
    # If the current combination is valid, return True
    return True

# Test the function with the sample input
n = 3
buttons = [
    ['Y', 'Y', 'Y'],
    ['N', 'Y', 'Y'],
    ['Y', 'N', 'Y']
]
max_times, combinations = get_max_times(n, buttons)
print(max_times)
for combination in combinations:
    print(*combination)

# Test the function with a larger input
n = 80
buttons = []
for i in range(n):
    buttons.append(list(input()))
max_times, combinations = get_max_times(n, buttons)
print(max_times)
for combination in combinations:
    print(*combination)

