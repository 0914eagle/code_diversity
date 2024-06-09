
def get_min_operations(n):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the series of amounts
    while current_amount < n:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # Increment the number of operations
            operations += 1
            # Add the current amount to the total amount
            current_amount += current_amount
        # If the current amount is not a multiple of 6 or 9, add 1 yen
        else:
            operations += 1
            current_amount += 1
    
    # Return the minimum number of operations required to withdraw the total amount
    return operations

def main():
    # Read the input from stdin
    n = int(input())
    
    # Call the get_min_operations function and print the result
    print(get_min_operations(n))

if __name__ == '__main__':
    main()

