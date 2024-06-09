
def solve(arr, operations):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each operation
    for operation in operations:
        # If the operation is to make an element equal to a specific value, perform the assignment
        if operation[0] == 1:
            arr[operation[1] - 1] = operation[2]
        # If the operation is to increase each element by a specific value, perform the assignment
        elif operation[0] == 2:
            arr = [x + operation[1] for x in arr]
        # If the operation is to take a piece of paper and write out the q-th array element, add the result to the list of results
        elif operation[0] == 3:
            results.append(arr[operation[1] - 1])
    
    # Return the list of results
    return results

