
def get_min_time(n, m, building):
    # Initialize variables
    total_time = 0
    current_floor = 0
    current_room = 0
    floors = []

    # Parse the building description
    for floor in building:
        floors.append(list(floor))

    # While there are still rooms with lights on
    while True:
        # Get the number of rooms with lights on in the current floor
        num_rooms_on = floors[current_floor].count("1")

        # If all rooms are off, move to the next floor
        if num_rooms_on == 0:
            total_time += 1
            current_floor += 1
            current_room = 0

            # If we have reached the last floor, break the loop
            if current_floor == n:
                break
        # Otherwise, turn off the light in the current room and move to the next room
        else:
            total_time += 1
            floors[current_floor][current_room] = "0"
            current_room += 1

            # If we have reached the last room in the current floor, move to the next floor
            if current_room == m:
                total_time += 1
                current_floor += 1
                current_room = 0

    return total_time

