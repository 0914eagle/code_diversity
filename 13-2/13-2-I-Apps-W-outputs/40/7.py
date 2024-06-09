
def solve(arr, operations):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the operations
    for operation in operations:
        # Check the type of operation
        if operation[0] == 1:
            # Make the v-th array element equal to x
            arr[operation[1] - 1] = operation[2]
        elif operation[0] == 2:
            # Increase each array element by y
            for i in range(len(arr)):
                arr[i] += operation[1]
        else:
            # Take a piece of paper and write out the q-th array element
            results.append(arr[operation[1] - 1])

    # Return the results
    return results

