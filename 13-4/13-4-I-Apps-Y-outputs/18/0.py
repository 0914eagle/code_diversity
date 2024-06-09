
import math

def get_angle(h, m):
    return (h * 30 + m / 2.0) % 360

def get_distance(a, b, h, m):
    angle = get_angle(h, m)
    return a * math.sin(math.radians(angle)) + b * math.cos(math.radians(angle))

def main():
    a, b, h, m = map(int, input().split())
    print(get_distance(a, b, h, m))

if __name__ == '__main__':
    main()

