
def get_min_distance(N, K, locations):
    # Sort the locations by their x-coordinate
    locations.sort(key=lambda x: x[0])

    # Initialize the variables
    current_location = 0
    total_distance = 0
    letters_delivered = 0

    # Loop through each location
    for location in locations:
        # Calculate the distance to the current location
        distance = abs(location[0] - current_location)

        # Check if the letters can be delivered in this trip
        if letters_delivered + location[1] <= K:
            # Add the distance to the total distance
            total_distance += distance

            # Update the letters delivered
            letters_delivered += location[1]

            # Update the current location
            current_location = location[0]
        else:
            # Calculate the distance to the next location
            next_location = locations[locations.index(location) + 1]
            next_distance = abs(next_location[0] - location[0])

            # Check if the letters can be delivered in this trip and the next trip
            if letters_delivered + location[1] + next_location[1] <= K:
                # Add the distance to the total distance
                total_distance += distance + next_distance

                # Update the letters delivered
                letters_delivered += location[1] + next_location[1]

                # Update the current location
                current_location = next_location[0]
            else:
                # Add the distance to the total distance
                total_distance += distance

                # Update the letters delivered
                letters_delivered += location[1]

                # Update the current location
                current_location = location[0]

    # Return the total distance
    return total_distance

