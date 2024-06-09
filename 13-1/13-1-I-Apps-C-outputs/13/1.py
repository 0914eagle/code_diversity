
def solve(A, K, Q):
    # Step 1: Sort the array A in non-decreasing order
    A.sort()
    # Step 2: Initialize the minimum difference as infinity
    min_diff = float('inf')
    # Step 3: Loop through each possible starting index for the contiguous subsequence
    for i in range(N-K+1):
        # Step 4: Find the maximum and minimum elements in the subsequence
        max_elem = max(A[i:i+K])
        min_elem = min(A[i:i+K])
        # Step 5: Update the minimum difference if necessary
        min_diff = min(min_diff, max_elem-min_elem)
    # Step 6: Return the minimum difference
    return min_diff

