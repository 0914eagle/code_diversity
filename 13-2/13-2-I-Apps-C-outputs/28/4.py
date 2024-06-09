
def solve(A, K, Q):
    # Step 1: Sort the input array
    A.sort()
    
    # Step 2: Initialize the minimum difference
    min_diff = float('inf')
    
    # Step 3: Loop through each possible contiguous subsequence of length K
    for i in range(len(A) - K + 1):
        # Step 3.1: Get the smallest element in the subsequence
        smallest = A[i]
        
        # Step 3.2: Get the largest element in the subsequence
        largest = A[i + K - 1]
        
        # Step 3.3: Calculate the difference between the smallest and largest element
        diff = largest - smallest
        
        # Step 3.4: Update the minimum difference
        min_diff = min(min_diff, diff)
    
    # Step 4: Return the minimum difference
    return min_diff

