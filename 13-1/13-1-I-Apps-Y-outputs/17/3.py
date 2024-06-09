
def get_min_operations(N):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the possible amounts
    for i in range(1, N+1):
        # Check if the current amount is a power of 6 or 9
        if i % 6 == 0 or i % 9 == 0:
            # If it is, add it to the current amount and increment the operations count
            current_amount += i
            operations += 1
    
    # Return the minimum number of operations required to reach the target amount
    return operations

