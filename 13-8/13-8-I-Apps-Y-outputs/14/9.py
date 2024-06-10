
def get_possible_orders(n, a):
    # Initialize a list to store the possible orders
    orders = []
    
    # Loop through each possible order
    for i in range(1, n + 1):
        # Check if the order is valid
        if is_valid_order(n, a, i):
            # Add the order to the list of possible orders
            orders.append(i)
    
    # Return the list of possible orders
    return orders

def is_valid_order(n, a, order):
    # Initialize a list to store the number of people to the left and right of each person
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    
    # Loop through each person and calculate the number of people to the left and right of them
    for i in range(1, n + 1):
        left[i] = left[i - 1] + (i - 1)
        right[i] = right[i - 1] + (n - i)
    
    # Loop through each person and check if the order is valid
    for i in range(1, n + 1):
        # Get the index of the person in the order
        index = order % n
        
        # Check if the number of people to the left and right of the person match the report
        if left[i] != a[index] or right[i] != a[(index + 1) % n]:
            # If the order is not valid, return False
            return False
        
        # Update the order and index for the next person
        order = order // n
        index = index // n
    
    # If all orders are valid, return True
    return True

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Get the possible orders
    orders = get_possible_orders(n, a)
    
    # Print the number of possible orders
    print(len(orders))

if __name__ == '__main__':
    main()

