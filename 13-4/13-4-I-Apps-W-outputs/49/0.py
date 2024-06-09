
def solve(recurrence, initial_values, queries):
    # Initialize the result list
    result = []
    
    # Create a dictionary to store the values of the recurrence
    values = {}
    
    # Populate the dictionary with the initial values
    for i in range(len(initial_values)):
        values[i] = initial_values[i]
    
    # Iterate through the queries
    for query in queries:
        # Initialize the current value to the initial value
        current_value = values[0]
        
        # Iterate through the recurrence
        for i in range(1, len(recurrence)):
            # Calculate the current value using the recurrence
            current_value += recurrence[i] * values[i - 1]
            
            # Store the current value in the dictionary
            values[i] = current_value
        
        # Add the result to the result list
        result.append(current_value % query[1])
    
    return result

