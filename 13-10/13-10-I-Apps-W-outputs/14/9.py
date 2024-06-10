
def get_distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def get_min_time(start, end, speed):
    return get_distance(start, end) / speed

def solve(a, b, n, cars):
    min_time = float('inf')
    for car in cars:
        time = get_min_time(a, car, cars[car])
        if time < min_time:
            min_time = time
    return min_time

def main():
    a, b = map(int, input().split())
    n = int(input())
    cars = {}
    for i in range(n):
        x, y, v = map(int, input().split())
        cars[(x, y)] = v
    print(solve(a, b, n, cars))

if __name__ == '__main__':
    main()

