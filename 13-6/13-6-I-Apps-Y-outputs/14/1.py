
def get_operations_required(amount):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the series of amounts
    for i in range(1, amount + 1):
        # Check if the current amount is a power of 6 or 9
        if i % 6 == 0 or i % 9 == 0:
            # If it is, add it to the current amount and increment the number of operations
            current_amount += i
            operations += 1
    
    # Return the number of operations required to reach the total amount
    return operations

def main():
    # Read the input amount from stdin
    amount = int(input())
    
    # Call the function to get the number of operations required
    operations = get_operations_required(amount)
    
    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

