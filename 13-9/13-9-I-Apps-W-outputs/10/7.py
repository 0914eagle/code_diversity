
def get_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def get_closest_taxi(home, taxis):
    min_distance = float('inf')
    closest_taxi = None
    for taxi in taxis:
        distance = get_distance(home, taxi)
        if distance < min_distance:
            min_distance = distance
            closest_taxi = taxi
    return closest_taxi

def get_time_to_arrive(home, taxi, speed):
    return get_distance(home, taxi) / speed

def get_min_time(home, taxis):
    min_time = float('inf')
    for taxi in taxis:
        time = get_time_to_arrive(home, taxi, taxi[2])
        if time < min_time:
            min_time = time
    return min_time

def solve(home, taxis):
    closest_taxi = get_closest_taxi(home, taxis)
    min_time = get_time_to_arrive(home, closest_taxi, closest_taxi[2])
    return min_time

def main():
    home = [int(x) for x in input().split()]
    n = int(input())
    taxis = []
    for i in range(n):
        taxis.append([int(x) for x in input().split()])
    print(solve(home, taxis))

if __name__ == '__main__':
    main()

