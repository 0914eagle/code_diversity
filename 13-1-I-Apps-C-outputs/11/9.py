
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
    
    # If we have operations left to perform on both arrays, iterate through them and calculate the minimum error
    if k_1 > 0 and k_2 > 0:
        for i in range(n):
            # If we have operations left to perform on array A, try increasing the current element by 1 and calculate the error
            if k_1 > 0:
                A[i] += 1
                k_1 -= 1
                current_error += (A[i] - B[i]) ** 2
                min_error = min(min_error, current_error)
                A[i] -= 1
                k_1 += 1
            
            # If we have operations left to perform on array B, try decreasing the current element by 1 and calculate the error
            if k_2 > 0:
                B[i] -= 1
                k_2 -= 1
                current_error += (A[i] - B[i]) ** 2
                min_error = min(min_error, current_error)
                B[i] += 1
                k_2 += 1
    
    # Return the minimum error
    return min_error

