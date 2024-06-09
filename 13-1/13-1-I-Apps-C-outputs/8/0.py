
def get_min_time(start, end, conveyors):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Loop through all possible combinations of walking on conveyors
    for conveyor_combination in itertools.product([0, 1], repeat=len(conveyors)):
        # Calculate the time for this combination of conveyors
        time = 0
        current_position = start
        for i, conveyor in enumerate(conveyors):
            # Check if the passenger is on a conveyor or not
            if conveyor_combination[i] == 1:
                # Calculate the time it takes to walk on the conveyor
                time += get_conveyor_time(current_position, conveyor)
                # Update the current position
                current_position = (conveyor[2], conveyor[3])
            else:
                # Calculate the time it takes to walk on the floor
                time += get_floor_time(current_position, conveyor)
                # Update the current position
                current_position = (conveyor[0], conveyor[1])
        
        # Check if the final time is less than the minimum time
        if time < min_time:
            min_time = time
    
    # Return the minimum time
    return min_time

def get_conveyor_time(start, conveyor):
    # Calculate the distance between the start and end of the conveyor
    distance = math.sqrt((conveyor[2] - conveyor[0]) ** 2 + (conveyor[3] - conveyor[1]) ** 2)
    # Return the time it takes to walk on the conveyor
    return distance / 2

def get_floor_time(start, conveyor):
    # Calculate the distance between the start and end of the conveyor
    distance = math.sqrt((conveyor[2] - conveyor[0]) ** 2 + (conveyor[3] - conveyor[1]) ** 2)
    # Return the time it takes to walk on the floor
    return distance

def main():
    # Read the input
    start, end = map(tuple, input().split())
    num_conveyors = int(input())
    conveyors = []
    for _ in range(num_conveyors):
        conveyors.append(tuple(map(float, input().split())))
    
    # Calculate the minimum time
    min_time = get_min_time(start, end, conveyors)
    
    # Print the minimum time
    print(min_time)

if __name__ == '__main__':
    main()

