
def get_min_time(start, end, conveyors):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Iterate over all possible combinations of walking on conveyors
    for conveyor_combination in itertools.product([0, 1], repeat=len(conveyors)):
        # Initialize the current time to 0
        current_time = 0
        
        # Iterate over the conveyors
        for i, conveyor in enumerate(conveyors):
            # If the current conveyor is used, add the time it takes to walk on it
            if conveyor_combination[i] == 1:
                current_time += get_conveyor_time(conveyor)
        
        # Add the time it takes to walk on the floor from the last conveyor to the end
        current_time += get_floor_time(end)
        
        # If the current time is less than the minimum time, update the minimum time
        if current_time < min_time:
            min_time = current_time
    
    return min_time

def get_conveyor_time(conveyor):
    # Return the time it takes to walk on the conveyor
    return abs(conveyor[1] - conveyor[0]) / 2

def get_floor_time(point):
    # Return the time it takes to walk on the floor from the current point to the end
    return abs(point[0])

def main():
    start, end = map(tuple, input().split())
    num_conveyors = int(input())
    conveyors = []
    for _ in range(num_conveyors):
        conveyors.append(tuple(map(float, input().split())))
    
    print(get_min_time(start, end, conveyors))

if __name__ == '__main__':
    main()

