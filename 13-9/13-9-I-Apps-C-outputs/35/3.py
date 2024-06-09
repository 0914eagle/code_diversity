
def longest_interesting_subsequence(A, S):
    
    # Initialize the result array
    result = [0] * len(A)

    # Loop through each element in the sequence
    for i in range(len(A)):
        # Calculate the sum of the first K elements
        sum1 = sum(A[:i+1])

        # Calculate the sum of the last K elements
        sum2 = sum(A[i:])

        # If neither sum is greater than S, the subsequence is interesting
        if sum1 <= S and sum2 <= S:
            # Set the length of the interesting subsequence starting with this element
            result[i] = i + 1

    return result

