
def solve(n, k_1, k_2, A, B):
    # Sort both arrays in non-decreasing order
    A.sort()
    B.sort()
    
    # Initialize the minimum error and the current error
    min_error = 0
    current_error = 0
    
    # Loop through both arrays and calculate the current error
    for i in range(n):
        current_error += (A[i] - B[i]) ** 2
    
    # If the current error is less than the minimum error, update the minimum error
    if current_error < min_error:
        min_error = current_error
    
    # Loop through the first array and perform the required number of operations
    for i in range(k_1):
        # Increment the first element of the first array by 1
        A[0] += 1
        # Calculate the new error
        current_error = 0
        for j in range(n):
            current_error += (A[j] - B[j]) ** 2
        # If the new error is less than the minimum error, update the minimum error
        if current_error < min_error:
            min_error = current_error
    
    # Loop through the second array and perform the required number of operations
    for i in range(k_2):
        # Increment the first element of the second array by 1
        B[0] += 1
        # Calculate the new error
        current_error = 0
        for j in range(n):
            current_error += (A[j] - B[j]) ** 2
        # If the new error is less than the minimum error, update the minimum error
        if current_error < min_error:
            min_error = current_error
    
    # Return the minimum error
    return min_error

