
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_position = 0
    direction = 1
    safety_island_position = 0
    safety_island_index = 0
    red_light_on = False

    # Loop through each second
    for second in range(1, n + 1):
        # Check if red light is on
        if second % (g + r) < g:
            red_light_on = True
        else:
            red_light_on = False

        # Check if safety island is reached
        if current_position in d:
            safety_island_position = current_position
            safety_island_index = d.index(current_position)

        # Check if it is possible to move
        if red_light_on and current_position not in d:
            return -1

        # Move in the direction of the current position
        current_position += direction

        # Check if the position is valid
        if current_position < 0 or current_position > n:
            return -1

        # Check if it is possible to change direction
        if current_position in d and safety_island_position != current_position:
            direction = -direction

        # Update the minimum time
        min_time += 1

    return min_time

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

