
def get_operations_required(N):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the possible amounts
    for amount in [1, 6, 9]:
        # Calculate the number of times we can withdraw this amount
        num_times = N // amount
        
        # Add the number of operations for this amount
        operations += num_times
        
        # Subtract the total amount withdrawn from the current amount
        current_amount -= num_times * amount
        
        # If we have withdrawn enough money, break the loop
        if current_amount <= 0:
            break
    
    # Return the number of operations required
    return operations

def main():
    # Read the input
    N = int(input())
    
    # Calculate the number of operations required
    operations = get_operations_required(N)
    
    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

