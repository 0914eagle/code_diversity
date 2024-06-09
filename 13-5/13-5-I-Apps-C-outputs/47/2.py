
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_time(distance, conveyor_speed):
    return distance / conveyor_speed

def get_optimal_path(start, end, conveyors):
    # Initialize the optimal path as the straight line path
    optimal_path = [start, end]
    optimal_time = get_time(get_distance(*start, *end), 1)

    # Iterate through all possible conveyor paths
    for conveyor in conveyors:
        # Get the start and end points of the conveyor
        start_conveyor, end_conveyor = conveyor[0], conveyor[1]

        # Get the straight line path from the start to the end of the conveyor
        straight_path = [start, end_conveyor]
        straight_time = get_time(get_distance(*start, *end_conveyor), 1)

        # Get the conveyor path from the start to the end of the conveyor
        conveyor_path = [start_conveyor, end_conveyor]
        conveyor_time = get_time(get_distance(*start_conveyor, *end_conveyor), 2)

        # Check if the conveyor path is faster than the straight line path
        if conveyor_time < straight_time:
            # Update the optimal path and time
            optimal_path = conveyor_path
            optimal_time = conveyor_time

    return optimal_path, optimal_time

def main():
    start, end = [float(x) for x in input().split()]
    num_conveyors = int(input())
    conveyors = []
    for _ in range(num_conveyors):
        conveyors.append([float(x) for x in input().split()])
    optimal_path, optimal_time = get_optimal_path((start, end), conveyors)
    print(optimal_time)

if __name__ == '__main__':
    main()

