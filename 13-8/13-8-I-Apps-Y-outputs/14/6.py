
def get_number_of_possible_orders(n, a):
    # Initialize a list to store the possible orders
    orders = []
    
    # Iterate over each possible order
    for i in range(1, n + 1):
        # Check if the order is valid
        if is_valid_order(n, a, i):
            # Add the order to the list of possible orders
            orders.append(i)
    
    # Return the number of possible orders
    return len(orders)

def is_valid_order(n, a, order):
    # Initialize a list to store the number of people standing to the left of each person
    left = [0] * (n + 1)
    
    # Iterate over each person
    for i in range(1, n + 1):
        # Get the number of people standing to the left of the current person
        left[i] = left[i - 1] + 1
        
        # Check if the current person is standing in the correct position
        if order == i:
            # Get the number of people standing to the right of the current person
            right = n - left[i]
            
            # Check if the number of people standing to the left of the current person is equal to the number of people standing to the right of the current person
            if left[i] == right:
                # The order is valid
                return True
    
    # The order is not valid
    return False

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Get the number of possible orders
    num_orders = get_number_of_possible_orders(n, a)
    
    # Print the number of possible orders
    print(num_orders)

if __name__ == '__main__':
    main()

