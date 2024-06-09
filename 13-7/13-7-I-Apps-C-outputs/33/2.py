
def get_average_visitors(n, a, p):
    # Calculate the sum of the guests' sizes
    total_size = sum(a)
    
    # Initialize a list to store the number of visitors for each possible order
    num_visitors = []
    
    # Iterate over all possible orders of the guests
    for order in permutations(range(1, n + 1)):
        # Initialize a variable to store the number of visitors for this order
        visitors = 0
        
        # Iterate over the guests in the order
        for i in order:
            # If the sum of the guests' sizes is less than or equal to the table length, increase the number of visitors
            if total_size <= p:
                visitors += 1
                total_size += a[i - 1]
        
        # Add the number of visitors for this order to the list
        num_visitors.append(visitors)
    
    # Return the average number of visitors
    return sum(num_visitors) / len(num_visitors)

