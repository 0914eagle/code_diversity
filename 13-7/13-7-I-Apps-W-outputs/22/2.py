
def solve(n, m, building):
    # Initialize variables
    total_time = 0
    current_floor = 0
    current_room = 0
    visited_rooms = set()

    # Iterate through each floor
    for floor in building:
        # Get the number of rooms in the current floor
        num_rooms = floor.count("1")

        # Iterate through each room in the current floor
        for room in range(num_rooms):
            # Check if the room has not been visited before
            if room not in visited_rooms:
                # Calculate the time it takes to go to the room
                time_to_room = abs(current_room - room)

                # Add the time to the total time
                total_time += time_to_room

                # Mark the room as visited
                visited_rooms.add(room)

                # Update the current room
                current_room = room

        # Calculate the time it takes to go to the next floor
        time_to_next_floor = abs(current_floor - (n - 1))

        # Add the time to the total time
        total_time += time_to_next_floor

        # Update the current floor
        current_floor = n - 1

    return total_time

