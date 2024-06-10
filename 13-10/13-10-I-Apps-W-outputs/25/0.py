
def get_elevator_time(start, end, floors, speed):
    
    start_floor = start[0]
    end_floor = end[0]
    floors_to_travel = abs(end_floor - start_floor)
    time_per_floor = floors_to_travel / speed
    return time_per_floor

def get_stairs_time(start, end):
    
    start_floor = start[0]
    end_floor = end[0]
    floors_to_travel = abs(end_floor - start_floor)
    return floors_to_travel

def get_time(start, end, floors, speed, stairs, elevators):
    
    if start[1] == end[1]:
        # Same floor, use stairs
        return get_stairs_time(start, end)
    elif start[0] == end[0]:
        # Same floor, use elevator
        return get_elevator_time(start, end, floors, speed)
    else:
        # Different floor, use elevator if possible
        if end[1] in elevators:
            return get_elevator_time(start, end, floors, speed)
        else:
            return get_stairs_time(start, end) + get_elevator_time((end[0], start[1]), end, floors, speed)

def main():
    n, m, c_l, c_e, v = map(int, input().split())
    l = list(map(int, input().split()))
    e = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    
    for query in queries:
        start = (query[0], query[1])
        end = (query[2], query[3])
        print(get_time(start, end, n, v, l, e))

if __name__ == '__main__':
    main()

