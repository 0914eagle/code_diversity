
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the result
    result = []

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if the current number is equal to i
        if i == n:
            # If the current number is equal to i, add it to the result
            result.append(i)
        else:
            # If the current number is not equal to i, add it to the result and then break the loop
            result.append(i)
            break

    # Return the result
    return result

