
def get_largest_sum(A, K):
    # Sort the array in non-decreasing order
    A.sort()
    
    # Initialize the sum of the array
    sum = 0
    
    # Loop through the array and calculate the sum
    for i in range(len(A)):
        sum += A[i]
    
    # Return the sum
    return sum
    
def get_largest_sum_after_modification(A, K):
    # Initialize the largest sum
    largest_sum = 0
    
    # Loop through the array and calculate the sum after modification
    for i in range(len(A)):
        # Calculate the sum of the array after modifying the ith element
        sum = 0
        for j in range(len(A)):
            if j == i:
                sum += -A[j]
            else:
                sum += A[j]
        
        # If the sum is larger than the largest sum, update the largest sum
        if sum > largest_sum:
            largest_sum = sum
    
    # Return the largest sum
    return largest_sum
    
if __name__ == '__main__':
    A = [4, 2, 3]
    K = 1
    print(get_largest_sum_after_modification(A, K))

