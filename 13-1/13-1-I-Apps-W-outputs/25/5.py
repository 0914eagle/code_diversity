
def get_min_time(n, m, building):
    # Initialize variables
    total_time = 0
    current_floor = 0
    current_room = 0
    visited_rooms = set()

    # Loop through each floor
    for floor in range(n):
        # Get the number of rooms in the current floor
        num_rooms = len(building[floor]) - 2

        # Loop through each room in the current floor
        for room in range(num_rooms):
            # Check if the room is visited before
            if room not in visited_rooms:
                # Calculate the time to visit the room
                time = abs(current_room - room)

                # Update the total time
                total_time += time

                # Update the current room and floor
                current_room = room
                current_floor = floor

                # Add the room to the visited set
                visited_rooms.add(room)

        # Calculate the time to go to the next floor
        time = abs(current_floor - floor)

        # Update the total time
        total_time += time

        # Update the current floor
        current_floor = floor

    return total_time

