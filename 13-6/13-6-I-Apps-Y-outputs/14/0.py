
def get_operations(N):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the possible amounts
    for amount in [1, 6, 9]:
        # Calculate the number of operations required for this amount
        num_operations = N // amount
        operations += num_operations
        current_amount += num_operations * amount
        
        # If we have already withdrawn more than the target amount, break the loop
        if current_amount > N:
            break
    
    return operations

def main():
    # Read the input
    N = int(input())
    
    # Calculate the number of operations required
    operations = get_operations(N)
    
    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

