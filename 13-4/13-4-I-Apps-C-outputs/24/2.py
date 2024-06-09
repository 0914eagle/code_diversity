
def solve(tickets):
    # Initialize the total tolls to 0
    total_tolls = 0

    # Loop through each ticket
    for ticket in tickets:
        # Get the entrance and exit numbers from the ticket
        entrance, exit = ticket

        # Calculate the toll for this ticket
        toll = abs(entrance - exit)

        # Add the toll to the total tolls
        total_tolls += toll

    # Return the least total amount of tolls
    return total_tolls

