
import math

def get_cheese_percentage(r, c):
    # Calculate the area of the crust
    crust_area = math.pi * (r - c) ** 2
    
    # Calculate the area of the pizza
    pizza_area = math.pi * r ** 2
    
    # Calculate the percentage of cheese
    cheese_percentage = 100 * (pizza_area - crust_area) / pizza_area
    
    return cheese_percentage

if __name__ == '__main__':
    r, c = map(int, input().split())
    print(get_cheese_percentage(r, c))

