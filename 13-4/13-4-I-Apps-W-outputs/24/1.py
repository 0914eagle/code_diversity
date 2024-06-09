
import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))

def count_subsequences(A, K):
    # Initialize the number of contiguous subsequences to 0
    count = 0
    
    # Iterate over the elements of A
    for i in range(len(A)):
        # Initialize the sum of the current subsequence to 0
        sum = 0
        
        # Iterate over the elements of A starting from the current element
        for j in range(i, len(A)):
            # Add the current element to the sum
            sum += A[j]
            
            # If the sum is greater than or equal to K, increment the count
            if sum >= K:
                count += 1
    
    return count

print(count_subsequences(A, K))

