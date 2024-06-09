
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_time(distance, speed):
    return distance / speed

def get_fastest_time(start, end, conveyors):
    # Initialize the fastest time to the time it takes to walk the entire distance
    fastest_time = get_time(get_distance(start[0], start[1], end[0], end[1]), 1)
    
    # Loop through each conveyor
    for conveyor in conveyors:
        # Get the distance from the start to the first point on the conveyor
        distance_to_conveyor = get_distance(start[0], start[1], conveyor[0], conveyor[1])
        
        # Get the distance from the first point on the conveyor to the second point on the conveyor
        conveyor_distance = get_distance(conveyor[0], conveyor[1], conveyor[2], conveyor[3])
        
        # Get the time it takes to walk from the start to the first point on the conveyor
        time_to_conveyor = get_time(distance_to_conveyor, 1)
        
        # Get the time it takes to walk on the conveyor
        conveyor_time = get_time(conveyor_distance, 2)
        
        # Get the time it takes to walk from the second point on the conveyor to the end
        time_from_conveyor = get_time(get_distance(conveyor[2], conveyor[3], end[0], end[1]), 1)
        
        # Calculate the total time it takes to walk on the conveyor and the time it takes to walk from the start to the end
        total_conveyor_time = time_to_conveyor + conveyor_time + time_from_conveyor
        total_time = time_to_conveyor + time_from_conveyor
        
        # Update the fastest time if the total time on the conveyor is faster than the fastest time
        if total_conveyor_time < fastest_time:
            fastest_time = total_conveyor_time
    
    return fastest_time

def main():
    start = [float(x) for x in input().split()]
    end = [float(x) for x in input().split()]
    num_conveyors = int(input())
    conveyors = []
    for _ in range(num_conveyors):
        conveyors.append([float(x) for x in input().split()])
    print(get_fastest_time(start, end, conveyors))

if __name__ == '__main__':
    main()

