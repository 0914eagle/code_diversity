
def get_min_time(start, end, conveyors):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Iterate over all possible combinations of walking on conveyors
    for conveyor_combination in itertools.product([0, 1], repeat=len(conveyors)):
        # Initialize the current time to 0
        current_time = 0
        
        # Iterate over the conveyors
        for i, conveyor in enumerate(conveyors):
            # If the current conveyor is being used, add the time it takes to walk on it
            if conveyor_combination[i] == 1:
                current_time += get_conveyor_time(conveyor)
        
        # Add the time it takes to walk on the floor from the start to the end
        current_time += get_floor_time(start, end)
        
        # If the current time is less than the minimum time, update the minimum time
        if current_time < min_time:
            min_time = current_time
    
    # Return the minimum time
    return min_time

def get_conveyor_time(conveyor):
    # Return the time it takes to walk on the conveyor
    return abs(conveyor[1] - conveyor[0]) / 2

def get_floor_time(start, end):
    # Return the time it takes to walk on the floor from start to end
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def main():
    # Read the input
    start, end = read_input()
    
    # Read the conveyors
    conveyors = []
    for _ in range(int(input())):
        conveyors.append(list(map(float, input().split())))
    
    # Get the minimum time
    min_time = get_min_time(start, end, conveyors)
    
    # Print the minimum time
    print(min_time)

def read_input():
    # Read the start and end coordinates
    start = list(map(float, input().split()))
    end = list(map(float, input().split()))
    
    # Return the start and end coordinates
    return start, end

if __name__ == '__main__':
    main()

