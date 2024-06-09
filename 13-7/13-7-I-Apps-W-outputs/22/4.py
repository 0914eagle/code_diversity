
def solve(n, m, building):
    # Initialize variables
    total_time = 0
    current_floor = 0
    current_room = 0
    rooms_visited = set()

    # Loop through each floor
    for floor in range(n):
        # Get the number of rooms in the current floor
        num_rooms = len(building[floor]) - 2

        # Loop through each room in the current floor
        for room in range(num_rooms):
            # Check if the light is on
            if building[floor][room + 1] == "1":
                # Calculate the time it takes to visit the room
                time_to_visit = abs(current_room - room)

                # Add the time to the total time
                total_time += time_to_visit

                # Update the current room and floor
                current_room = room
                current_floor = floor

                # Add the room to the set of visited rooms
                rooms_visited.add((current_floor, current_room))

    # Return the total time
    return total_time

