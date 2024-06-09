
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_time(distance):
    return distance / 2

def get_fastest_time(start, end, conveyors):
    min_time = get_time(get_distance(start[0], start[1], end[0], end[1]))
    for conveyor in conveyors:
        conveyor_time = get_time(get_distance(start[0], start[1], conveyor[0], conveyor[1])) + get_time(get_distance(conveyor[0], conveyor[1], conveyor[2], conveyor[3])) + get_time(get_distance(conveyor[2], conveyor[3], end[0], end[1]))
        if conveyor_time < min_time:
            min_time = conveyor_time
    return min_time

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

