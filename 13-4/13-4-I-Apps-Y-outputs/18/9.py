
import math

def get_angle(h, m):
    
    hour_angle = (h / 12.0) * 360.0
    minute_angle = (m / 60.0) * 360.0
    return abs(hour_angle - minute_angle)

def get_distance(a, b, h, m):
    
    angle = get_angle(h, m)
    return a * math.sin(math.radians(angle)) + b * math.cos(math.radians(angle))

def main():
    a, b, h, m = map(int, input().split())
    print(get_distance(a, b, h, m))

if __name__ == '__main__':
    main()

