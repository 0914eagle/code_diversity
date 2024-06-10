
import math

def get_time_taken(d, s):
    return d / s

def get_distance(d, s, t):
    return d + s * t

def get_speed(d, s, t):
    return d / t

def get_constant_speed(d, s, t):
    time_taken = get_time_taken(d, s)
    distance = get_distance(d, s, time_taken)
    speed = get_speed(distance, time_taken)
    return speed - s

def main():
    n, t = map(int, input().split())
    distance = 0
    speedometer_readings = []
    for _ in range(n):
        distance, speedometer_reading = map(int, input().split())
        speedometer_readings.append(speedometer_reading)
    constant_speed = get_constant_speed(distance, speedometer_readings, t)
    print(constant_speed)

if __name__ == '__main__':
    main()

