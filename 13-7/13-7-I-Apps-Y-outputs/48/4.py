
import math

def get_circle_area(radius, geometry="euclidian"):
    if geometry == "euclidian":
        return math.pi * radius ** 2
    elif geometry == "taxicab":
        return 2 * radius ** 2
    else:
        raise ValueError("Invalid geometry")

def main():
    radius = int(input())
    print(get_circle_area(radius))
    print(get_circle_area(radius, "taxicab"))

if __name__ == '__main__':
    main()

