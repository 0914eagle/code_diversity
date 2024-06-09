
def get_operations_required(amount):
    # Initialize variables
    operations = 0
    current_amount = 0
    
    # Loop through the amounts in descending order
    for i in range(amount, 0, -1):
        # If the current amount plus the current amount is less than or equal to the target amount, add the current amount to the current amount and increment the operations count
        if current_amount + i <= amount:
            current_amount += i
            operations += 1
    
    # Return the operations count
    return operations

def main():
    # Read the input amount from stdin
    amount = int(input())
    
    # Call the get_operations_required function and print the result
    print(get_operations_required(amount))

if __name__ == '__main__':
    main()

