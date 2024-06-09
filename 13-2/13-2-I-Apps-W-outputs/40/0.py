
def solve(arr, operations):
    # Initialize an empty list to store the results
    results = []

    # Loop through each operation
    for operation in operations:
        # If the operation is of type 1, set the value at the specified index to the specified value
        if operation[0] == 1:
            arr[operation[1] - 1] = operation[2]
        # If the operation is of type 2, increase each value by the specified amount
        elif operation[0] == 2:
            for i in range(len(arr)):
                arr[i] += operation[1]
        # If the operation is of type 3, print the value at the specified index
        elif operation[0] == 3:
            results.append(arr[operation[1] - 1])

    # Return the results
    return results

