
def solve(A, B, k, m):
    # Check if k and m are valid indices for the arrays
    if k > len(A) or m > len(B):
        return "NO"
    
    # Initialize two pointers for the arrays
    i = 0
    j = 0
    
    # Loop through the arrays until we reach the end of either array
    while i < k and j < m:
        # If the current element of A is less than the current element of B,
        # we can choose the current element of A and move on to the next element of A
        if A[i] < B[j]:
            i += 1
        # If the current element of A is greater than or equal to the current element of B,
        # we can choose the current element of B and move on to the next element of B
        elif A[i] >= B[j]:
            j += 1
        # If we reach the end of either array, return "NO"
        if i == k or j == m:
            return "NO"
    
    # If we reach this point, it means that we were able to choose k elements in A and m elements in B
    # such that any element chosen in A is strictly less than any element chosen in B
    return "YES"

