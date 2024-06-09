
def solve(N, M, A, B, C):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each operation
    for j in range(M):
        # Initialize a sum for this operation to 0
        operation_sum = 0
        # Loop through each card
        for i in range(N):
            # Check if the card is chosen for this operation
            if B[j] > 0:
                # Add the value of the card to the operation sum
                operation_sum += A[i]
                # Decrement the number of cards chosen for this operation
                B[j] -= 1
        # Add the operation sum to the maximum sum
        max_sum += operation_sum
        # Loop through each card
        for i in range(N):
            # Check if the card is chosen for this operation
            if B[j] > 0:
                # Replace the value of the card with the new value
                A[i] = C[j]
                # Decrement the number of cards chosen for this operation
                B[j] -= 1
    # Return the maximum sum
    return max_sum

