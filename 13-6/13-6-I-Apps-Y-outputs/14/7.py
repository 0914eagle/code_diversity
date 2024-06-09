
def get_withdrawal_operations(n):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the possible withdrawal amounts
    for i in range(1, n + 1):
        # Check if the current amount is a power of 6 or 9
        if i % 6 == 0 or i % 9 == 0:
            # Increment the number of operations
            operations += 1
            # Add the current amount to the total amount withdrawn
            current_amount += i
            
            # Check if the total amount withdrawn is equal to the target amount
            if current_amount == n:
                # If it is, return the number of operations
                return operations
    
    # If the target amount could not be reached, return -1
    return -1

def main():
    # Read the target amount from standard input
    n = int(input())
    
    # Call the get_withdrawal_operations function and print the result
    print(get_withdrawal_operations(n))

if __name__ == '__main__':
    main()

