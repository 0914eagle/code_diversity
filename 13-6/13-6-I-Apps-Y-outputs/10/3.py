
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
    
def modify_array(A, K):
    # Initialize a list to store the indices of the elements to be modified
    indices = []
    
    # Loop through the array and find the indices of the elements to be modified
    for i in range(len(A)):
        if A[i] < 0:
            indices.append(i)
    
    # Loop through the list of indices and modify the corresponding elements of the array
    for i in indices:
        A[i] = -A[i]
    
    # Return the modified array
    return A
    
if __name__ == '__main__':
    A = [4, 2, 3]
    K = 1
    print(get_largest_sum(A, K))
    print(modify_array(A, K))

