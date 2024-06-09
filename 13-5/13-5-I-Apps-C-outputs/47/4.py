
def get_time(start, end, conveyors):
    # Calculate the distance between start and end points
    distance = ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5

    # Initialize the time needed to travel the distance
    time = distance

    # Loop through each conveyor
    for conveyor in conveyors:
        # Calculate the distance between the start point and the conveyor
        conveyor_distance = ((conveyor[0] - start[0]) ** 2 + (conveyor[1] - start[1]) ** 2) ** 0.5

        # Calculate the distance between the end point and the conveyor
        end_conveyor_distance = ((conveyor[2] - end[0]) ** 2 + (conveyor[3] - end[1]) ** 2) ** 0.5

        # Check if the start point is on the conveyor
        if conveyor_distance < 1:
            # If the start point is on the conveyor, calculate the time needed to travel the distance on the conveyor
            time += distance - conveyor_distance

        # Check if the end point is on the conveyor
        if end_conveyor_distance < 1:
            # If the end point is on the conveyor, calculate the time needed to travel the distance on the conveyor
            time += end_conveyor_distance

    return time

def main():
    start, end = [float(i) for i in input().split()]
    num_conveyors = int(input())
    conveyors = []
    for _ in range(num_conveyors):
        conveyors.append([float(i) for i in input().split()])
    print(get_time((start, end), conveyors))

if __name__ == '__main__':
    main()

