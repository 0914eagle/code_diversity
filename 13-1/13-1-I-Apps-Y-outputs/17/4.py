
def f1(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # Loop until the target amount is reached
    while current_amount < N:
        # Check if the current amount is a multiple of 6 or 9
        if current_amount % 6 == 0 or current_amount % 9 == 0:
            # If it is, add the appropriate amount
            current_amount += current_amount % 6 == 0 and 6 or 9
        else:
            # If it's not, add 1 yen
            current_amount += 1

        # Increment the number of operations
        operations += 1

    # Return the number of operations required
    return operations

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N = int(input())
    print(f1(N))

