
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
            # Check if the light is on
            if building[floor][room + 1] == "1":
                # Calculate the time to turn off the light
                time = abs(current_floor - floor) + abs(current_room - room)

                # Update the total time
                total_time += time

                # Update the current floor and room
                current_floor = floor
                current_room = room

                # Add the room to the visited set
                visited_rooms.add((current_floor, current_room))

    return total_time

def main():
    n, m = map(int, input().split())
    building = [input() for _ in range(n)]
    print(get_min_time(n, m, building))

if __name__ == '__main__':
    main()

