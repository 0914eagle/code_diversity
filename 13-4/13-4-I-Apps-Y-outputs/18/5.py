
import math

def get_angle(h, m):
    
    angle_hour = (h / 12) * 360
    angle_minute = (m / 60) * 360
    return abs(angle_hour - angle_minute)

def get_distance(a, b, angle):
    
    return a * math.sin(math.radians(angle)) + b * math.cos(math.radians(angle))

def main():
    a, b, h, m = map(int, input().split())
    angle = get_angle(h, m)
    distance = get_distance(a, b, angle)
    print(distance)

if __name__ == '__main__':
    main()

