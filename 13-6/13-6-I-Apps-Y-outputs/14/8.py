
def get_operations_required(amount):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the amounts in descending order
    for i in range(amount, 0, -1):
        # Check if the current amount is a multiple of the current amount
        if amount % i == 0:
            # Increment the number of operations
            operations += 1
            # Add the current amount to the total amount withdrawn
            current_amount += i
            # Update the amount left to withdraw
            amount = amount - current_amount
    
    return operations

def main():
    # Read the amount to withdraw from standard input
    amount = int(input())
    # Call the function to get the number of operations required
    operations = get_operations_required(amount)
    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

