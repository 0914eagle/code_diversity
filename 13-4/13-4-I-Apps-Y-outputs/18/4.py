
import math

def get_angle(h, m):
    # Calculate the angle between the hour and minute hands
    hour_angle = (h / 12.0) * 360.0
    minute_angle = (m / 60.0) * 360.0
    angle = abs(hour_angle - minute_angle)
    return angle

def get_distance(a, b, angle):
    # Calculate the distance between the unfixed endpoints of the hands
    distance = a * math.sin(math.radians(angle)) + b * math.cos(math.radians(angle))
    return distance

def main():
    a, b, h, m = map(int, input().split())
    angle = get_angle(h, m)
    distance = get_distance(a, b, angle)
    print(distance)

if __name__ == '__main__':
    main()

