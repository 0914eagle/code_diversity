
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_time(distance, speed):
    return distance / speed

def get_fastest_time(start, end, conveyors):
    # Initialize variables
    fastest_time = get_time(get_distance(start[0], start[1], end[0], end[1]), 1)
    current_position = start
    current_speed = 1

    # Iterate through each conveyor
    for conveyor in conveyors:
        # Check if the current position is on the conveyor
        if current_position[0] >= conveyor[0] and current_position[0] <= conveyor[2] and current_position[1] >= conveyor[1] and current_position[1] <= conveyor[3]:
            # If the current position is on the conveyor, calculate the time it takes to walk the length of the conveyor
            conveyor_time = get_time(get_distance(current_position[0], current_position[1], conveyor[2], conveyor[3]), 2)
            # If the time on the conveyor is faster than the fastest time, update the fastest time
            if conveyor_time < fastest_time:
                fastest_time = conveyor_time
            # Update the current position and speed
            current_position = (conveyor[2], conveyor[3])
            current_speed = 2
        # If the current position is not on the conveyor, calculate the time it takes to walk to the next point on the conveyor
        else:
            next_point = None
            for i in range(len(conveyors)):
                if conveyors[i][0] <= current_position[0] <= conveyors[i][2] and conveyors[i][1] <= current_position[1] <= conveyors[i][3]:
                    next_point = (conveyors[i][0], conveyors[i][1]) if current_position[0] < conveyors[i][0] else (conveyors[i][2], conveyors[i][3])
                    break
            if next_point:
                walk_time = get_time(get_distance(current_position[0], current_position[1], next_point[0], next_point[1]), current_speed)
                if walk_time + conveyor_time < fastest_time:
                    fastest_time = walk_time + conveyor_time
                    current_position = next_point
                    current_speed = 2

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

