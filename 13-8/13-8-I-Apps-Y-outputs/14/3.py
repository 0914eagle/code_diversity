
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
    # Initialize a set to store the numbers that have already been used
    used_numbers = set()
    
    # Iterate over each number in the order
    for i in range(n):
        # Check if the number has already been used
        if order[i] in used_numbers:
            # If the number has already been used, return False
            return False
        # Add the number to the set of used numbers
        used_numbers.add(order[i])
    
    # If all numbers are unique, return True
    return True

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

