
def get_valid_scenarios(n, k, x):
    # Initialize a set to store the valid scenarios
    valid_scenarios = set()
    
    # Iterate over each question
    for i in range(k):
        # Get the current and next cell numbers
        curr_cell = x[i]
        next_cell = x[(i+1) % k]
        
        # If the current cell and next cell are adjacent, add the scenario to the set
        if abs(curr_cell - next_cell) == 1:
            valid_scenarios.add((curr_cell, next_cell))
    
    # Return the number of valid scenarios
    return len(valid_scenarios)

def main():
    # Read the input
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    
    # Get the number of valid scenarios
    valid_scenarios = get_valid_scenarios(n, k, x)
    
    # Print the number of valid scenarios
    print(valid_scenarios)

if __name__ == '__main__':
    main()

