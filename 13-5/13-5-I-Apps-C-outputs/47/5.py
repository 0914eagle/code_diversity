
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_time(distance, speed):
    return distance / speed

def get_fastest_time(start, end, conveyors):
    # Initialize the fastest time to the time it takes to walk from start to end directly
    fastest_time = get_time(get_distance(start[0], start[1], end[0], end[1]), 1)
    
    # Iterate over the conveyors
    for conveyor in conveyors:
        # Get the start and end points of the conveyor
        start_point = (conveyor[0], conveyor[1])
        end_point = (conveyor[2], conveyor[3])
        
        # Get the distance from the start point to the end point of the conveyor
        conveyor_distance = get_distance(start_point[0], start_point[1], end_point[0], end_point[1])
        
        # Get the time it takes to walk from the start point to the end point of the conveyor
        conveyor_time = get_time(conveyor_distance, 2)
        
        # Get the distance from the start point to the end point, considering the conveyor
        total_distance = get_distance(start[0], start[1], end[0], end[1]) + conveyor_distance
        
        # Get the time it takes to walk from the start point to the end point, considering the conveyor
        total_time = get_time(total_distance, 1) + conveyor_time
        
        # Update the fastest time if the current conveyor is faster
        if total_time < fastest_time:
            fastest_time = total_time
    
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

