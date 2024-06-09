
def get_minimum_time(n, m, building):
    # Initialize variables
    total_time = 0
    current_floor = 0
    current_room = 0
    visited_rooms = set()

    # Loop through each floor
    for floor in building:
        # Loop through each room in the floor
        for room in range(m):
            # If the light is on and we haven't visited this room before, turn it off and update the variables
            if floor[room] == "1" and room not in visited_rooms:
                total_time += 1
                visited_rooms.add(room)
                current_room = room
                break

        # If we've visited all the rooms in this floor, go to the next floor
        if current_room == m - 1:
            total_time += 1
            current_floor += 1
            current_room = 0

    return total_time

