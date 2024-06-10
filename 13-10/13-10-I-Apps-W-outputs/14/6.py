
def find_min_time(point, cars):
    min_time = float('inf')
    for car in cars:
        time = abs(point[0] - car[0]) / car[2] + abs(point[1] - car[1]) / car[2]
        min_time = min(min_time, time)
    return min_time

def solve(point, cars):
    return find_min_time(point, cars)

