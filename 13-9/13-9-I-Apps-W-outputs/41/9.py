
def compute_speed(distance, speedometer_reading):
    return distance / speedometer_reading

def compute_constant(segments):
    distances = [segment[0] for segment in segments]
    speedometer_readings = [segment[1] for segment in segments]
    speeds = [compute_speed(distance, speedometer_reading) for distance, speedometer_reading in zip(distances, speedometer_readings)]
    true_speeds = [speed + compute_speed(distance, 0) for speed, distance in zip(speeds, distances)]
    return sum(true_speeds) / sum(distances)

def main():
    n, t = map(int, input().split())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    c = compute_constant(segments)
    print(c)

if __name__ == '__main__':
    main()

