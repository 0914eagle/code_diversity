
import math

def f1(R, C):
    # Calculate the area of the crust
    crust_area = math.pi * C ** 2
    
    # Calculate the area of the pizza
    pizza_area = math.pi * R ** 2
    
    # Calculate the percentage of cheese
    cheese_percentage = (pizza_area - crust_area) / pizza_area
    
    return cheese_percentage

def f2(R, C):
    # Calculate the area of the crust
    crust_area = math.pi * C ** 2
    
    # Calculate the area of the pizza
    pizza_area = math.pi * R ** 2
    
    # Calculate the percentage of cheese
    cheese_percentage = (pizza_area - crust_area) / pizza_area
    
    return cheese_percentage

if __name__ == '__main__':
    R, C = map(int, input().split())
    print(f1(R, C))
    print(f2(R, C))

