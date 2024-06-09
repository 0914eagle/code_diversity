
def solve(N, trucks):
    # Initialize a dictionary to store the tolls for each truck
    tolls = {}
    # Iterate over the trucks
    for truck in trucks:
        # Get the entrance and exit numbers for the current truck
        entrance, exit = truck
        # If the truck has not been processed before
        if entrance not in tolls:
            # Add the toll for the current truck to the dictionary
            tolls[entrance] = abs(entrance - exit)
        # If the truck has been processed before
        else:
            # Get the current toll for the truck
            current_toll = tolls[entrance]
            # Get the new toll for the truck
            new_toll = abs(entrance - exit)
            # Update the toll for the truck if the new toll is lower
            if new_toll < current_toll:
                tolls[entrance] = new_toll
    # Return the sum of the tolls for all trucks
    return sum(tolls.values())

