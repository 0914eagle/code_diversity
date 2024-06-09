
def get_minimum_time(n, m, building):
    # Initialize variables
    total_time = 0
    current_floor = 0
    current_room = 0

    # Loop through each floor
    for floor in range(n):
        # Get the number of rooms in the current floor
        num_rooms = len(building[floor]) - 2

        # Loop through each room in the current floor
        for room in range(num_rooms):
            # Check if the light is on
            if building[floor][room + 1] == "1":
                # Calculate the time to go to the current room
                time = abs(current_room - room)

                # Update the total time
                total_time += time

                # Update the current room
                current_room = room

                # Update the current floor
                current_floor = floor

                # Break the loop
                break

        # Update the current floor
        current_floor += 1

        # Update the current room
        current_room = 0

    # Return the total time
    return total_time

