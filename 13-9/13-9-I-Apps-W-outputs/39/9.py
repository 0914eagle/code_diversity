
def get_valid_scenarios(n, k, questions):
    # Initialize a set to store the valid scenarios
    valid_scenarios = set()
    
    # Iterate over each question
    for i in range(k):
        # Get the current and next cell numbers
        current_cell = questions[i]
        next_cell = questions[(i + 1) % k]
        
        # If the current cell is not equal to the next cell, add the scenario to the set
        if current_cell != next_cell:
            valid_scenarios.add((current_cell, next_cell))
    
    # Return the number of valid scenarios
    return len(valid_scenarios)

def main():
    # Read the input data
    n, k = map(int, input().split())
    questions = list(map(int, input().split()))
    
    # Call the get_valid_scenarios function and print the result
    print(get_valid_scenarios(n, k, questions))

if __name__ == '__main__':
    main()

