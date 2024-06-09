
def get_largest_sum(A, K):
    # Sort the array in non-decreasing order
    A.sort()
    
    # Initialize the sum of the array
    sum = 0
    
    # Iterate through the array and calculate the sum
    for i in range(len(A)):
        sum += A[i]
    
    # Return the sum
    return sum
    
def get_largest_sum_after_modification(A, K):
    # Initialize the sum of the array
    sum = 0
    
    # Iterate through the array and calculate the sum
    for i in range(len(A)):
        sum += A[i]
    
    # Return the sum
    return sum
    
if __name__ == '__main__':
    A = [4, 2, 3]
    K = 1
    print(get_largest_sum_after_modification(A, K))

