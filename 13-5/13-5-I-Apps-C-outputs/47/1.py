
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_time(distance, conveyor_speed):
    return distance / conveyor_speed

def get_fastest_time(start, end, conveyors):
    # Initialize variables
    fastest_time = get_time(get_distance(start[0], start[1], end[0], end[1]), 1)
    current_time = 0
    current_position = start

    # Iterate through each conveyor
    for conveyor in conveyors:
        # Get the distance to the start of the conveyor
        distance_to_start = get_distance(current_position[0], current_position[1], conveyor[0], conveyor[1])

        # Add the time it takes to walk to the start of the conveyor
        current_time += get_time(distance_to_start, 1)

        # Add the time it takes to walk on the conveyor
        current_time += get_time(get_distance(conveyor[0], conveyor[1], conveyor[2], conveyor[3]), 2)

        # Get the distance to the end of the conveyor
        distance_to_end = get_distance(conveyor[2], conveyor[3], end[0], end[1])

        # Add the time it takes to walk to the end of the conveyor
        current_time += get_time(distance_to_end, 1)

        # Update the fastest time if the current time is less than the fastest time
        if current_time < fastest_time:
            fastest_time = current_time

        # Update the current position to the end of the conveyor
        current_position = (conveyor[2], conveyor[3])

    return fastest_time

def main():
    start = tuple(map(float, input().split()))
    end = tuple(map(float, input().split()))
    num_conveyors = int(input())
    conveyors = []
    for _ in range(num_conveyors):
        conveyors.append(tuple(map(float, input().split())))
    print(get_fastest_time(start, end, conveyors))

if __name__ == '__main__':
    main()

