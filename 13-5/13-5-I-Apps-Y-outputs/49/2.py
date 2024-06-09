
def solve(N, A):
    # Initialize a variable to store the maximum number of operations
    max_operations = 0
    # Loop through the array of integers
    for i in range(N):
        # Check if the current integer is even
        if A[i] % 2 == 0:
            # If it is even, divide it by 2
            A[i] //= 2
            # Increment the maximum number of operations
            max_operations += 1
    # Return the maximum number of operations
    return max_operations

