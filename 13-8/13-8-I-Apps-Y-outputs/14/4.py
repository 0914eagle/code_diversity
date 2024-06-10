
def get_possible_orders(n, a):
    # Initialize a list to store the possible orders
    orders = []
    
    # Iterate over each possible order
    for i in range(1, n + 1):
        # Check if the order is valid
        if is_valid_order(n, a, i):
            # Add the order to the list of possible orders
            orders.append(i)
    
    # Return the list of possible orders
    return orders

def is_valid_order(n, a, order):
    # Initialize a flag to indicate if the order is valid
    valid = True
    
    # Iterate over each person
    for i in range(1, n + 1):
        # Calculate the number of people to the left and right of the current person
        left = order - i
        right = n - i + 1
        
        # Check if the difference between the number of people to the left and right is correct
        if abs(left - right) != a[i - 1]:
            # If the difference is not correct, set the flag to False
            valid = False
            break
    
    # Return the flag
    return valid

def main():
    # Read the input from stdin
    n = int(input())
    a = list(map(int, input().split()))
    
    # Get the possible orders
    orders = get_possible_orders(n, a)
    
    # Print the number of possible orders
    print(len(orders))

if __name__ == '__main__':
    main()

