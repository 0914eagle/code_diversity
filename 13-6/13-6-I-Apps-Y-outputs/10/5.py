
def get_largest_sum(A, K):
    # Sort the array in non-decreasing order
    A.sort()
    
    # Initialize the sum of the array
    sum_array = sum(A)
    
    # Loop through each element in the array
    for i in range(len(A)):
        # If the element is negative, flip it to positive
        if A[i] < 0:
            A[i] = -A[i]
        
        # If the element is still negative after flipping, break the loop
        if A[i] < 0:
            break
    
    # Return the sum of the array
    return sum_array
    
def get_largest_sum_k_times(A, K):
    # Initialize the sum of the array
    sum_array = 0
    
    # Loop through each iteration of K
    for i in range(K):
        # Get the largest sum of the array after modifying it
        sum_array = max(sum_array, get_largest_sum(A, K))
    
    # Return the largest sum of the array after K iterations
    return sum_array
    
if __name__ == '__main__':
    A = [4, 2, 3]
    K = 1
    print(get_largest_sum_k_times(A, K))


