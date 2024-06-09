
def solve(n, guests, p):
    # Calculate the total number of possible orders
    num_orders = 1
    for i in range(n):
        num_orders *= n - i
    
    # Initialize the sum of guests in the restaurant to 0
    sum_guests = 0
    
    # Initialize the number of guests in the restaurant to 0
    num_guests = 0
    
    # Initialize the number of guests who have come to the restaurant to 0
    num_visitors = 0
    
    # Iterate over all possible orders of the guests
    for order in itertools.permutations(guests):
        # Iterate over the guests in the order
        for i, guest in enumerate(order):
            # Check if the guest fits in the restaurant
            if sum_guests + guest <= p:
                # Add the guest to the restaurant
                sum_guests += guest
                num_guests += 1
            else:
                # The guest doesn't fit in the restaurant, break the loop
                break
        
        # Check if all guests have fit in the restaurant
        if num_guests == n:
            # Add the number of visitors to the total
            num_visitors += 1
        
        # Remove the guests from the restaurant
        sum_guests -= order[0]
        num_guests -= 1
    
    # Return the average number of visitors
    return num_visitors / num_orders

