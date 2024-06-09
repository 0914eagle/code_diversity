
def get_min_time(start, end, conveyors):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Iterate over all possible combinations of walking on conveyors
    for conveyor_combination in itertools.product([0, 1], repeat=len(conveyors)):
        # Initialize the current time to 0
        current_time = 0
        
        # Iterate over the conveyors
        for i, conveyor in enumerate(conveyors):
            # If the current conveyor is being used, add the conveyor time to the current time
            if conveyor_combination[i]:
                current_time += get_conveyor_time(conveyor)
        
        # Add the time to walk on the floor between the last conveyor and the end point
        current_time += get_floor_time(end, conveyors[-1][1])
        
        # If the current time is less than the minimum time, update the minimum time
        if current_time < min_time:
            min_time = current_time
    
    return min_time

def get_conveyor_time(conveyor):
    # Return the time to walk on the conveyor
    return abs(conveyor[1][0] - conveyor[0][0]) / 2

def get_floor_time(end, start):
    # Return the time to walk on the floor between the start and end points
    return abs(end[0] - start[0])

def main():
    start, end = map(lambda x: tuple(map(float, x.split())), input().split(','))
    num_conveyors = int(input())
    conveyors = [tuple(map(float, input().split(','))) for _ in range(num_conveyors)]
    print(get_min_time(start, end, conveyors))

if __name__ == '__main__':
    main()

