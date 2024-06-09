
def get_operations_required(amount):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the amounts
    while current_amount < amount:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # If it is, add it to the current amount
            current_amount += current_amount
            # Increment the number of operations
            operations += 1
        # If it is not, add 1 yen
        else:
            current_amount += 1
            operations += 1
    
    # Return the number of operations required
    return operations

def main():
    # Read the amount from stdin
    amount = int(input())
    
    # Call the function to get the number of operations required
    operations = get_operations_required(amount)
    
    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

