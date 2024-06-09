
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_time(distance, speed):
    return distance / speed

def get_fastest_time(start, end, conveyors):
    # Initialize the fastest time to the time it would take to walk from start to end
    fastest_time = get_time(get_distance(start[0], start[1], end[0], end[1]), 1)
    
    # Iterate over the conveyors and calculate the time it would take to walk on each conveyor and the time it would take to walk from the start to the end of the conveyor and back to the start
    for conveyor in conveyors:
        conveyor_distance = get_distance(conveyor[0], conveyor[1], conveyor[2], conveyor[3])
        conveyor_time = get_time(conveyor_distance, 2)
        total_time = conveyor_time + get_time(get_distance(start[0], start[1], conveyor[0], conveyor[1]), 1) + get_time(get_distance(conveyor[2], conveyor[3], end[0], end[1]), 1)
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

