
def get_operations_required(n):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the series of operations
    while current_amount < n:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # If it is, add the current amount to the total amount
            current_amount += current_amount
            # Increment the number of operations
            operations += 1
        # If the current amount is not a multiple of 6 or 9, add 1 yen
        else:
            current_amount += 1
            operations += 1
    
    # Return the number of operations required
    return operations

def main():
    # Read the input
    n = int(input())
    
    # Call the function to get the number of operations required
    operations = get_operations_required(n)
    
    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

