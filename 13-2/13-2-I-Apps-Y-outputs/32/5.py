
import math

def get_percentage_cheese(radius, crust_thickness):
    # Calculate the total area of the pizza
    total_area = math.pi * radius ** 2
    
    # Calculate the area of the crust
    crust_area = math.pi * (radius - crust_thickness) ** 2
    
    # Calculate the area of the cheese
    cheese_area = total_area - crust_area
    
    # Calculate the percentage of cheese
    percentage_cheese = cheese_area / total_area
    
    return percentage_cheese

if __name__ == '__main__':
    radius, crust_thickness = map(int, input().split())
    print(get_percentage_cheese(radius, crust_thickness))

