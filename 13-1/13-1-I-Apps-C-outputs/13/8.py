
def solve(A, K, Q):
    # Step 1: Sort the input array
    A.sort()
    
    # Step 2: Initialize the minimum difference
    min_diff = float('inf')
    
    # Step 3: Loop through each possible starting index
    for i in range(N-K+1):
        # Step 4: Initialize the maximum and minimum values
        max_val = -float('inf')
        min_val = float('inf')
        
        # Step 5: Loop through each element in the subsequence
        for j in range(K):
            # Step 6: Update the maximum and minimum values
            max_val = max(max_val, A[i+j])
            min_val = min(min_val, A[i+j])
        
        # Step 7: Calculate the difference and update the minimum difference
        diff = max_val - min_val
        min_diff = min(min_diff, diff)
    
    # Step 8: Return the minimum difference
    return min_diff

