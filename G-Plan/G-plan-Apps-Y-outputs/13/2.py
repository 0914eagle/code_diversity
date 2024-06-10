
import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

def input_radius():
    return int(input())

if __name__ == "__main__":
    radius = input_radius()
    circumference = calculate_circumference(radius)
    print(f"{circumference:.20f}")
