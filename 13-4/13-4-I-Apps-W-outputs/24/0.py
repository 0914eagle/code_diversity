
def solve(A, K):
    # Calculate the prefix sum of the array
    prefix_sum = [0]
    for i in range(len(A)):
        prefix_sum.append(prefix_sum[i] + A[i])

    # Initialize the number of contiguous subsequences to 0
    count = 0

    # Iterate through the prefix sum array
    for i in range(len(prefix_sum)):
        # Check if the prefix sum at index i is greater than or equal to K
        if prefix_sum[i] >= K:
            # Increment the number of contiguous subsequences
            count += 1

    # Return the number of contiguous subsequences
    return count

