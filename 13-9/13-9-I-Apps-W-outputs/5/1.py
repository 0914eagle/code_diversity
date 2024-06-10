
def get_lamp_combinations(n, k, lamps):
    # Base case: if k is 1, return all lamps
    if k == 1:
        return [[l] for l in lamps]
    
    # Initialize an empty list to store combinations
    combinations = []
    
    # Iterate over all possible combinations of k lamps
    for i in range(n - k + 1):
        # Get the current combination of k lamps
        current_combination = lamps[i:i+k]
        
        # If the current combination is valid, add it to the list of combinations
        if is_valid_combination(current_combination):
            combinations.append(current_combination)
    
    return combinations

def is_valid_combination(combination):
    # Initialize a set to store the times when lamps are turned on
    lamp_times = set()
    
    # Iterate over all lamps in the combination
    for lamp in combination:
        # Add the lamp's turning on time to the set of lamp times
        lamp_times.add(lamp[0])
        lamp_times.add(lamp[1])
    
    # If the set of lamp times has only one element, the combination is valid
    return len(lamp_times) == 1

def get_number_of_valid_combinations(n, k, lamps):
    # Get all valid combinations of k lamps
    valid_combinations = get_lamp_combinations(n, k, lamps)
    
    # Return the number of valid combinations
    return len(valid_combinations)

def main():
    # Read the input
    n, k = map(int, input().split())
    lamps = []
    for _ in range(n):
        l, r = map(int, input().split())
        lamps.append([l, r])
    
    # Get the number of valid combinations of k lamps
    valid_combinations = get_number_of_valid_combinations(n, k, lamps)
    
    # Print the answer modulo 998244353
    print(valid_combinations % 998244353)

if __name__ == '__main__':
    main()

