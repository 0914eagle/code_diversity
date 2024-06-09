
import math

def get_circumference(radius):
    return 2 * math.pi * radius

if __name__ == '__main__':
    radius = float(input())
    print(get_circumference(radius))

