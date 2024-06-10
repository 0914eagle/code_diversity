
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_pos = 0
    current_dir = 1
    safety_islands = set(d)
    green_light = True

    # Iterate until Denis reaches the end of the road
    while current_pos != n:
        # If the red light is on, Denis must be on a safety island
        if not green_light and current_pos not in safety_islands:
            return -1

        # If Denis is on a safety island, he can change direction
        if current_pos in safety_islands:
            current_dir = -current_dir

        # Move Denis in the current direction
        current_pos += current_dir

        # Update the time and the green light status
        min_time += 1
        green_light = not green_light

    # Return the minimum time
    return min_time

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

