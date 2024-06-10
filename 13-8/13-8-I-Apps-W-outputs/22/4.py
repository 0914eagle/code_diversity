
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_position = 0
    current_direction = 1
    safety_islands = set(d)
    safety_islands.add(0)
    safety_islands.add(n)

    # Iterate over the green lights
    while current_position < n:
        # Move to the next green light
        min_time += g
        current_position += current_direction

        # Check if we need to change direction
        if current_position in safety_islands:
            current_direction *= -1

        # Check if we reached the end of the road
        if current_position == n:
            break

        # Wait for the red light
        min_time += r

    # Return the minimum time
    return min_time

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

