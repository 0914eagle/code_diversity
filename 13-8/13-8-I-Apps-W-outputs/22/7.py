
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_position = 0
    previous_position = 0
    safety_island_index = 0
    safety_island_coordinates = d
    green_light_on = True
    red_light_on = False
    safety_island_reached = False
    impossible = False

    # Loop through each second
    for i in range(n):
        # Check if green light is on
        if green_light_on:
            # Check if safety island reached
            if safety_island_reached:
                # Change direction of movement
                if previous_position == 0:
                    current_position += 1
                elif previous_position == n - 1:
                    current_position -= 1
                else:
                    current_position += 1
                    safety_island_reached = False

            # Check if current position is a safety island
            if current_position in safety_island_coordinates:
                safety_island_reached = True

            # Update previous position
            previous_position = current_position

            # Update time
            min_time += 1

        # Check if red light is on
        elif red_light_on:
            # Check if safety island reached
            if safety_island_reached:
                # Change direction of movement
                if previous_position == 0:
                    current_position += 1
                elif previous_position == n - 1:
                    current_position -= 1
                else:
                    current_position += 1
                    safety_island_reached = False

            # Check if current position is a safety island
            if current_position in safety_island_coordinates:
                safety_island_reached = True

            # Update previous position
            previous_position = current_position

            # Update time
            min_time += 1

        # Check if green light is off and red light is off
        else:
            # Check if safety island reached
            if safety_island_reached:
                # Change direction of movement
                if previous_position == 0:
                    current_position += 1
                elif previous_position == n - 1:
                    current_position -= 1
                else:
                    current_position += 1
                    safety_island_reached = False

            # Check if current position is a safety island
            if current_position in safety_island_coordinates:
                safety_island_reached = True

            # Update previous position
            previous_position = current_position

            # Update time
            min_time += 1

        # Update green and red light status
        green_light_on = not green_light_on
        red_light_on = not red_light_on

    # Check if impossible to cross the road
    if current_position != n:
        impossible = True

    # Return minimum time or -1 if impossible
    if impossible:
        return -1
    else:
        return min_time

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

