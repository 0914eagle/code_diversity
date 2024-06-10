
def get_valid_scenarios(n, k, questions):
    # Initialize a set to store the valid scenarios
    valid_scenarios = set()
    
    # Iterate over each question
    for i in range(k):
        # Get the current question
        question = questions[i]
        
        # If this is the first question, add the starting scenario (1, question) to the valid scenarios
        if i == 0:
            valid_scenarios.add((1, question))
        
        # If this is not the first question, iterate over the current valid scenarios
        else:
            # Get the current valid scenarios
            current_valid_scenarios = set(valid_scenarios)
            
            # Iterate over the current valid scenarios
            for scenario in current_valid_scenarios:
                # Get the starting cell and ending cell of the scenario
                starting_cell, ending_cell = scenario
                
                # If the starting cell is not the same as the question, add the new scenario (starting_cell, question) to the valid scenarios
                if starting_cell != question:
                    valid_scenarios.add((starting_cell, question))
                
                # If the ending cell is not the same as the question, add the new scenario (question, ending_cell) to the valid scenarios
                if ending_cell != question:
                    valid_scenarios.add((question, ending_cell))
    
    # Return the number of valid scenarios
    return len(valid_scenarios)

def get_number_of_scenarios(n, k, questions):
    # Get the valid scenarios
    valid_scenarios = get_valid_scenarios(n, k, questions)
    
    # Initialize a set to store the unique scenarios
    unique_scenarios = set()
    
    # Iterate over the valid scenarios
    for scenario in valid_scenarios:
        # Get the starting cell and ending cell of the scenario
        starting_cell, ending_cell = scenario
        
        # If the starting cell is not the same as the ending cell, add the scenario to the unique scenarios
        if starting_cell != ending_cell:
            unique_scenarios.add(scenario)
    
    # Return the number of unique scenarios
    return len(unique_scenarios)

def main():
    # Read the input
    n, k = map(int, input().split())
    questions = list(map(int, input().split()))
    
    # Call the function to get the number of scenarios
    number_of_scenarios = get_number_of_scenarios(n, k, questions)
    
    # Print the number of scenarios
    print(number_of_scenarios)

if __name__ == '__main__':
    main()

