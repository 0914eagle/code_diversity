
def get_max_times(n, buttons):
    # Initialize a list to store the results
    results = []
    
    # Iterate over each possible combination of buttons
    for combination in itertools.permutations(range(n)):
        # Check if the current combination is valid
        if is_valid_combination(combination, buttons):
            # If it is valid, add it to the results list
            results.append(list(combination))
    
    # Return the maximum number of times and the corresponding combinations
    return len(results), results

def is_valid_combination(combination, buttons):
    # Check if the current combination is valid
    for i in range(len(combination)):
        for j in range(i+1, len(combination)):
            if combination[i] == combination[j] and buttons[i][j] == 'N':
                return False
    return True

n = int(input())
buttons = []
for i in range(n):
    buttons.append(input())

max_times, combinations = get_max_times(n, buttons)
print(max_times)
for combination in combinations:
    print(*combination)

