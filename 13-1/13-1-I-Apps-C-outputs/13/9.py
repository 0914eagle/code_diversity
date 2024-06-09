
def solve(A, K, Q):
    # Step 1: Sort the input array
    A.sort()
    
    # Step 2: Initialize the minimum difference
    min_diff = float('inf')
    
    # Step 3: Loop through each possible subsequence
    for i in range(len(A) - K + 1):
        # Step 3.1: Get the subsequence
        subsequence = A[i:i+K]
        
        # Step 3.2: Get the minimum element in the subsequence
        min_element = subsequence[0]
        
        # Step 3.3: Get the maximum element in the subsequence
        max_element = subsequence[-1]
        
        # Step 3.4: Calculate the difference between the maximum and minimum elements
        diff = max_element - min_element
        
        # Step 3.5: Update the minimum difference
        min_diff = min(min_diff, diff)
    
    # Step 4: Return the minimum difference
    return min_diff

