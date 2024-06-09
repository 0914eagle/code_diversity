
def solve(n, k_1, k_2, A, B):
    # Calculate the initial error
    error = sum((a - b) ** 2 for a, b in zip(A, B))
    # Loop through the operations for array A
    for i in range(k_1):
        # Find the element with the largest difference between A and B
        max_diff = max(abs(a - b) for a, b in zip(A, B))
        # Find the index of the element with the largest difference
        max_index = A.index(max_diff)
        # Increment or decrement the element by 1 depending on which array has the largest difference
        if A[max_index] > B[max_index]:
            A[max_index] -= 1
        else:
            A[max_index] += 1
    # Loop through the operations for array B
    for i in range(k_2):
        # Find the element with the largest difference between A and B
        max_diff = max(abs(a - b) for a, b in zip(A, B))
        # Find the index of the element with the largest difference
        max_index = B.index(max_diff)
        # Increment or decrement the element by 1 depending on which array has the largest difference
        if A[max_index] > B[max_index]:
            B[max_index] += 1
        else:
            B[max_index] -= 1
    # Calculate the final error
    error = sum((a - b) ** 2 for a, b in zip(A, B))
    return error

