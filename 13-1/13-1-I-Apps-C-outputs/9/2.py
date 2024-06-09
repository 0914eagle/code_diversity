
def solve(n, k_1, k_2, A, B):
    # Sort both arrays in non-decreasing order
    A.sort()
    B.sort()
    
    # Initialize the minimum error and the current error
    min_error = float('inf')
    current_error = 0
    
    # Loop through all possible combinations of moves for arrays A and B
    for i in range(k_1 + 1):
        for j in range(k_2 + 1):
            # Calculate the current error
            current_error = 0
            for k in range(n):
                current_error += (A[k] - B[k]) ** 2
            
            # If the current error is less than the minimum error, update the minimum error
            if current_error < min_error:
                min_error = current_error
    
    # Return the minimum error
    return min_error

