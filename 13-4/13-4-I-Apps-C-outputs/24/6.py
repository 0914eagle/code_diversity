
def solve(tickets):
    # Initialize a dictionary to store the tolls for each exit
    tolls = {}
    # Initialize the total tolls to 0
    total_tolls = 0
    # Iterate over the tickets
    for ticket in tickets:
        # Get the entrance and exit numbers from the ticket
        entrance, exit = ticket
        # If the exit is not already in the dictionary, add it with a toll of 0
        if exit not in tolls:
            tolls[exit] = 0
        # Calculate the toll for the exit
        toll = abs(entrance - exit)
        # Add the toll to the total tolls
        total_tolls += toll
        # If the entrance is not already in the dictionary, add it with a toll of 0
        if entrance not in tolls:
            tolls[entrance] = 0
        # Add the toll to the total tolls
        total_tolls += toll
        # Update the toll for the exit
        tolls[exit] += toll
    # Return the least total amount of tolls
    return total_tolls

