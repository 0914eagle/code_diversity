
def solve(n, guests, p):
    # Calculate the sum of the guests' sizes
    total_size = sum(guests)
    
    # Initialize a list to store the number of guests that can fit in the restaurant
    num_guests = []
    
    # Iterate over the possible orders of the guests
    for order in permutations(guests):
        # Initialize a variable to store the current size of the restaurant
        current_size = 0
        
        # Iterate over the guests in the current order
        for guest in order:
            # Check if the current size of the restaurant plus the size of the current guest is less than or equal to the table length
            if current_size + guest <= p:
                # Add the size of the current guest to the current size of the restaurant
                current_size += guest
            else:
                # If the current size of the restaurant plus the size of the current guest is greater than the table length, break the loop
                break
        
        # If the current size of the restaurant is equal to the total size of all guests, all guests can fit in the restaurant
        if current_size == total_size:
            # Add the number of guests to the list
            num_guests.append(len(guests))
    
    # Return the average number of guests that can fit in the restaurant
    return sum(num_guests) / len(num_guests)

