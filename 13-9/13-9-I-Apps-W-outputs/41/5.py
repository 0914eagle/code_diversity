
def get_time_from_distance(d, v):
    return d / v

def get_distance_from_time(t, v):
    return v * t

def get_speedometer_reading(d, t, v):
    return d / t

def get_true_speed(s, c):
    return s + c

def get_constant_c(n, t, distances, speeds):
    total_distance = sum(distances)
    total_time = t
    for i in range(n):
        distance = distances[i]
        time = get_time_from_distance(distance, speeds[i])
        speed = get_speedometer_reading(distance, time)
        true_speed = get_true_speed(speed, c)
        total_distance -= distance
        total_time -= time
    return (total_distance / total_time) - c

def main():
    n, t = map(int, input().split())
    distances = []
    speeds = []
    for i in range(n):
        distance, speed = map(int, input().split())
        distances.append(distance)
        speeds.append(speed)
    c = get_constant_c(n, t, distances, speeds)
    print(c)

if __name__ == '__main__':
    main()

