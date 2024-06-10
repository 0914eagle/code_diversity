
def get_true_speed(speed, time):
    return speed * time

def get_distance(speed, time):
    return speed * time

def get_constant(segments):
    total_distance = 0
    total_time = 0
    for segment in segments:
        distance = get_distance(segment[1], segment[0])
        time = segment[0]
        total_distance += distance
        total_time += time

    avg_speed = total_distance / total_time
    return avg_speed - segments[0][1]

def main():
    n, t = map(int, input().split())
    segments = []
    for i in range(n):
        d, s = map(int, input().split())
        segments.append((d, s))
    c = get_constant(segments)
    print(c)

if __name__ == '__main__':
    main()

