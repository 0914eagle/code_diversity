
import math

def get_radius(r, c):
    return r - c

def get_circumference(r):
    return 2 * math.pi * r

def get_cheese_percentage(r, c):
    radius = get_radius(r, c)
    circumference = get_circumference(radius)
    return circumference / (2 * math.pi * r)

def main():
    r, c = map(int, input().split())
    print(get_cheese_percentage(r, c))

if __name__ == '__main__':
    main()

