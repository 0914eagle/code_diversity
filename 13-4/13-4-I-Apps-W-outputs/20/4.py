
def find_permutation(n):
    # Initialize a list to store the permutation
    permutation = []

    # Iterate from 1 to N
    for i in range(1, n + 1):
        # Check if the current number is not equal to its index
        if i != n:
            # Add the current number to the permutation
            permutation.append(i)
        # If the current number is equal to its index, find the next number that is not equal to its index
        else:
            # Iterate from the current number to N
            for j in range(i, n + 1):
                # Check if the current number is not equal to its index
                if j != n:
                    # Add the current number to the permutation
                    permutation.append(j)
                    break

    # Return the permutation
    return permutation

