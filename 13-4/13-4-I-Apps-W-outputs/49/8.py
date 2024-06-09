
def solve_recurrence(recurrence, initial_values, queries):
    # Initialize the results dictionary
    results = {}
    
    # Loop through each query
    for query in queries:
        # Get the index and modulus
        index, modulus = query
        
        # Check if the result is already calculated
        if index in results:
            # If so, return the result
            result = results[index]
        else:
            # If not, calculate the result using the recurrence relation
            result = calculate_result(recurrence, initial_values, index)
            results[index] = result
        
        # Print the result modulo the modulus
        print(result % modulus)

def calculate_result(recurrence, initial_values, index):
    # Initialize the result
    result = initial_values[0]
    
    # Loop through each term in the recurrence relation
    for i in range(1, len(recurrence)):
        # Calculate the term
        term = recurrence[i] * calculate_result(recurrence, initial_values, index - i)
        
        # Add the term to the result
        result += term
    
    # Return the result
    return result

# Test the function with example inputs
recurrence = [0, 1, 1]
initial_values = [0, 1]
queries = [(1, 100000), (2, 100000), (3, 100000), (4, 100000), (5, 100000), (6, 100000)]
solve_recurrence(recurrence, initial_values, queries)

recurrence = [5, 7, 9]
initial_values = [36713, 5637282]
queries = [(1, 10000), (1375, 1), (3781, 23), (34683447233, 1571385)]
solve_recurrence(recurrence, initial_values, queries)

