
def solve(n, k_1, k_2, A, B):
    # Calculate the initial error
    error = sum((a - b) ** 2 for a, b in zip(A, B))
    # Loop through the operations for array A
    for i in range(k_1):
        # Find the index of the minimum element in A
        min_index = A.index(min(A))
        # Increment the minimum element by 1
        A[min_index] += 1
        # Calculate the new error
        error += (A[min_index] - B[min_index]) ** 2
    # Loop through the operations for array B
    for i in range(k_2):
        # Find the index of the minimum element in B
        min_index = B.index(min(B))
        # Decrement the minimum element by 1
        B[min_index] -= 1
        # Calculate the new error
        error += (A[min_index] - B[min_index]) ** 2
    # Return the minimum possible error
    return error

