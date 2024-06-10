
import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

def main():
    radius = int(input())
    circumference = calculate_circumference(radius)
    print("{:.20f}".format(circumference))

if __name__ == "__main__":
    main()
