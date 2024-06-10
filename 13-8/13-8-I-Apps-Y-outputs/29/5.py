
import math

def get_pizza_info():
    
    radius, crust_thickness = map(int, input().split())
    return radius, crust_thickness

def get_percentage_of_cheese(radius, crust_thickness):
    
    # Calculate the area of the pizza
    pizza_area = math.pi * radius ** 2
    
    # Calculate the area of the crust
    crust_area = math.pi * (radius - crust_thickness) ** 2
    
    # Calculate the percentage of cheese
    percentage_of_cheese = 100 * (pizza_area - crust_area) / pizza_area
    
    return percentage_of_cheese

def main():
    radius, crust_thickness = get_pizza_info()
    percentage_of_cheese = get_percentage_of_cheese(radius, crust_thickness)
    print(f"{percentage_of_cheese:.10f}")

if __name__ == '__main__':
    main()

