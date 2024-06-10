
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_position = 0
    current_direction = 1
    safety_islands = set(d)
    safety_islands.add(0)
    safety_islands.add(n)

    # Loop until the end of the road is reached
    while current_position != n:
        # If the current position is a safety island, change the direction
        if current_position in safety_islands:
            current_direction *= -1

        # Move forward by 1 unit
        current_position += current_direction
        min_time += 1

        # If the red light is on, wait for it to turn green
        if current_position in safety_islands:
            min_time += g

    # Return the minimum time
    return min_time

def main():
    n, m = map(int, input().split())
    d = set(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

