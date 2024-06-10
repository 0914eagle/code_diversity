
def get_possible_orders(N, A):
    # Initialize a list to store the possible orders
    orders = []
    
    # Iterate over each possible order
    for i in range(N):
        # Check if the order is valid
        if is_valid_order(N, A, i):
            # Add the order to the list of possible orders
            orders.append(i)
    
    # Return the list of possible orders
    return orders

def is_valid_order(N, A, order):
    # Initialize a boolean variable to store the result
    valid = True
    
    # Iterate over each person
    for i in range(N):
        # Calculate the number of people to the left and right of the current person
        left = (order - i - 1) % N
        right = (i - order) % N
        
        # Check if the absolute difference is correct
        if abs(left - right) != A[i]:
            # The order is not valid
            valid = False
            break
    
    # Return the result
    return valid

def main():
    # Read the input
    N = int(input())
    A = list(map(int, input().split()))
    
    # Get the possible orders
    orders = get_possible_orders(N, A)
    
    # Print the number of possible orders
    print(len(orders))

if __name__ == '__main__':
    main()

