
import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

def main():
    radius = int(input())
    circumference = calculate_circumference(radius)
    print(f"{circumference:.20f}")

if __name__ == "__main__":
    main()
