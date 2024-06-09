
def get_possible_orders(n, a):
    # Initialize a list to store the possible orders
    orders = []
    
    # Loop through each possible order
    for i in range(1, n + 1):
        # Check if the order is valid
        if is_valid_order(i, n, a):
            # Add the order to the list
            orders.append(i)
    
    # Return the list of possible orders
    return orders

def is_valid_order(order, n, a):
    # Initialize a set to store the numbers that have already been used
    used_numbers = set()
    
    # Loop through each number in the order
    for i in range(n):
        # Get the number of the person standing to the left of the current person
        left_person = (i - 1) % n + 1
        
        # Get the number of the person standing to the right of the current person
        right_person = (i + 1) % n + 1
        
        # Check if the current person is standing between the two people
        if left_person != order[i - 1] and right_person != order[i - 1]:
            # Return False if the current person is not standing between the two people
            return False
        
        # Add the current person's number to the set of used numbers
        used_numbers.add(order[i - 1])
    
    # Return True if all the numbers have been used
    return len(used_numbers) == n

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

