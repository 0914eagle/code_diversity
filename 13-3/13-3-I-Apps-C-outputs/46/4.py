
def f1(n, positions):
    # Initialize a dictionary to store the results
    results = {}
    
    # Iterate over each position
    for position in positions:
        # Initialize a set to store the available options
        options = set()
        
        # Iterate over each option
        for option in position:
            # Add the option to the set of available options
            options.add(option)
        
        # Add the set of available options to the dictionary
        results[position] = options
    
    # Return the dictionary of results
    return results

def f2(n, positions, start_position):
    # Initialize a dictionary to store the results
    results = {}
    
    # Iterate over each position
    for position in positions:
        # Initialize a set to store the available options
        options = set()
        
        # Iterate over each option
        for option in position:
            # Add the option to the set of available options
            options.add(option)
        
        # Add the set of available options to the dictionary
        results[position] = options
    
    # Return the dictionary of results
    return results

if __name__ == '__main__':
    n = int(input())
    positions = [input().split() for _ in range(n)]
    start_position = input()
    results = f1(n, positions)
    print(f2(n, positions, start_position))

