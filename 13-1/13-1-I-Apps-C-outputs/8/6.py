
def get_min_time(start, end, conveyors):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Loop through all possible combinations of conveyors
    for conveyor_combination in itertools.product([0, 1], repeat=len(conveyors)):
        # Calculate the time for this combination of conveyors
        time = 0
        current_position = start
        for i, conveyor in enumerate(conveyors):
            # If the conveyor is used, move along it
            if conveyor_combination[i] == 1:
                time += get_time_on_conveyor(current_position, conveyor)
                current_position = (conveyor[0], conveyor[1])
            # If the conveyor is not used, move on the floor
            else:
                time += get_time_on_floor(current_position, conveyor)
                current_position = (conveyor[0], conveyor[1])
        
        # If the final position is reached, calculate the total time
        if current_position == end:
            min_time = min(min_time, time)
    
    # Return the minimum time
    return min_time

def get_time_on_conveyor(start, conveyor):
    # Calculate the distance to the end of the conveyor
    distance = math.sqrt((conveyor[0] - start[0])**2 + (conveyor[1] - start[1])**2)
    # Return the time it takes to travel the distance on the conveyor
    return distance / 2

def get_time_on_floor(start, end):
    # Calculate the distance to the end of the floor
    distance = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    # Return the time it takes to travel the distance on the floor
    return distance

def main():
    start, end = map(tuple, input().split())
    num_conveyors = int(input())
    conveyors = []
    for _ in range(num_conveyors):
        conveyors.append(tuple(map(float, input().split())))
    
    print(get_min_time(start, end, conveyors))

if __name__ == "__main__":
    main()

