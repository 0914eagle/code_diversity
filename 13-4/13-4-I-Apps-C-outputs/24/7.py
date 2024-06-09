
def get_least_total_tolls(trucks):
    # Initialize a dictionary to store the tolls for each truck
    tolls = {}
    # Iterate over the trucks
    for truck in trucks:
        # Get the entrance and exit numbers for the current truck
        entrance, exit = truck
        # If the entrance and exit numbers are not the same
        if entrance != exit:
            # Calculate the toll for the current truck
            toll = abs(entrance - exit)
            # Add the toll to the dictionary
            tolls[truck] = toll
    # Initialize a set to store the exchanged tickets
    exchanged_tickets = set()
    # Initialize a variable to store the total tolls
    total_tolls = 0
    # Iterate until all tickets are exchanged
    while len(tolls) > 0:
        # Find the two tickets with the minimum tolls that have not been exchanged yet
        min_toll = min(tolls, key=tolls.get)
        # Get the entrance and exit numbers for the first truck
        entrance1, exit1 = min_toll
        # Remove the first truck from the dictionary
        del tolls[min_toll]
        # Find the second truck with the minimum tolls that has not been exchanged yet
        min_toll = min(tolls, key=tolls.get)
        # Get the entrance and exit numbers for the second truck
        entrance2, exit2 = min_toll
        # Remove the second truck from the dictionary
        del tolls[min_toll]
        # Calculate the total tolls for the two trucks
        total_tolls += tolls[min_toll]
        # Add the exchanged tickets to the set
        exchanged_tickets.add(min_toll)
        # Add the exchanged tickets to the set
        exchanged_tickets.add((entrance1, exit2))
        exchanged_tickets.add((entrance2, exit1))
    # Return the total tolls
    return total_tolls

