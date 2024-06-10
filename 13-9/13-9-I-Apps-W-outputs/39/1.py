
def get_number_of_scenarios(n, k, x):
    # Initialize a dictionary to store the number of scenarios for each position
    scenarios = {}
    
    # Iterate over all possible positions
    for i in range(1, n+1):
        # Initialize the number of scenarios for the current position to 0
        scenarios[i] = 0
        
        # Iterate over all possible questions
        for j in range(k):
            # If the current position is one of the questions, increment the number of scenarios by 1
            if i == x[j]:
                scenarios[i] += 1
    
    # Return the total number of scenarios
    return sum(scenarios.values())

def main():
    # Read the input data
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    
    # Call the function to get the number of scenarios
    result = get_number_of_scenarios(n, k, x)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

