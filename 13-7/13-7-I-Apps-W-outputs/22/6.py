
def get_minimum_time(n, m, building):
    # Initialize variables
    total_time = 0
    current_floor = 0
    current_room = 0
    rooms_per_floor = m + 2
    floors = n

    # Loop through each floor
    for floor in range(floors):
        # Get the current floor's building description
        floor_building = building[floor]

        # Loop through each room in the current floor
        for room in range(rooms_per_floor):
            # Check if the light is on
            if floor_building[room] == "1":
                # Calculate the time it takes to turn off the light
                time = abs(current_room - room)

                # Update the total time
                total_time += time

                # Update the current room
                current_room = room

                # Break out of the loop
                break

        # Update the current floor
        current_floor += 1

    # Return the total time
    return total_time

