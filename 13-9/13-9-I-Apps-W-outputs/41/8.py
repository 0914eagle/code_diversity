
def get_constant_speedometer(d, s):
    return s - d

def get_true_speed(d, s, c):
    return s + c

def get_constant_from_journey(segments):
    distances = [segment[0] for segment in segments]
    speedometer_readings = [segment[1] for segment in segments]
    true_speeds = [get_true_speed(d, s, 0) for d, s in zip(distances, speedometer_readings)]
    constant_speeds = [get_constant_speedometer(d, s) for d, s in zip(distances, true_speeds)]
    constant = sum(constant_speeds) / len(constant_speeds)
    return constant

def main():
    n, t = map(int, input().split())
    segments = []
    for _ in range(n):
        d, s = map(int, input().split())
        segments.append((d, s))
    constant = get_constant_from_journey(segments)
    print(f"{constant:.9f}")

if __name__ == '__main__':
    main()

