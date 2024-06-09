
def get_maximum_divisible(A, K):
    # Sort the array in non-decreasing order
    A.sort()
    
    # Initialize the maximum divisible number as 1
    max_divisible = 1
    
    # Loop through each element of the array
    for i in range(len(A)):
        # Check if the current element is divisible by the maximum divisible number
        if A[i] % max_divisible == 0:
            # If it is divisible, update the maximum divisible number
            max_divisible = max(max_divisible, A[i])
        else:
            # If it is not divisible, find the smallest number that is divisible by the current element
            # and is less than or equal to the current element
            for j in range(max_divisible, A[i] + 1):
                if A[i] % j == 0:
                    max_divisible = j
                    break
    
    # Return the maximum divisible number
    return max_divisible

