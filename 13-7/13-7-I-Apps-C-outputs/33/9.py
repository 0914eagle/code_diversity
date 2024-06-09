
def solve(n, guests, p):
    # Calculate the sum of the guests' sizes
    total_size = sum(guests)
    
    # Initialize a variable to store the number of guests who have come to the restaurant
    num_guests = 0
    
    # Iterate over the possible orders of the guests
    for order in permutations(guests):
        # Initialize a variable to store the size of the guests who have come to the restaurant
        current_size = 0
        
        # Iterate over the guests in the current order
        for guest in order:
            # Check if the current guest fits in the restaurant
            if current_size + guest <= p:
                # Increment the number of guests who have come to the restaurant
                num_guests += 1
                # Increment the size of the guests who have come to the restaurant
                current_size += guest
            else:
                # Break out of the loop if the current guest doesn't fit in the restaurant
                break
    
    # Return the average number of guests who have come to the restaurant
    return num_guests / n!

