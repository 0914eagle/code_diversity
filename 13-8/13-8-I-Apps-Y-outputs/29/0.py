
import math

def calculate_area(radius, crust_width):
    
    return math.pi * radius ** 2 - (math.pi * (radius - crust_width) ** 2)

def calculate_percentage(area, total_area):
    
    return 100 * area / total_area

def main():
    radius, crust_width = map(float, input().split())
    area = calculate_area(radius, crust_width)
    total_area = math.pi * radius ** 2
    percentage = calculate_percentage(area, total_area)
    print(f"{percentage:.6f}")

if __name__ == '__main__':
    main()

