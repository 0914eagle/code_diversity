
import math

def f1(R, C):
    # Calculate the area of the crust
    area_crust = math.pi * C ** 2
    
    # Calculate the area of the pizza
    area_pizza = math.pi * R ** 2
    
    # Calculate the percentage of cheese
    percentage_cheese = 100 * (area_pizza - area_crust) / area_pizza
    
    return percentage_cheese

def f2(R, C):
    # Calculate the area of the crust
    area_crust = math.pi * C ** 2
    
    # Calculate the area of the pizza
    area_pizza = math.pi * R ** 2
    
    # Calculate the percentage of cheese
    percentage_cheese = 100 * (area_pizza - area_crust) / area_pizza
    
    return percentage_cheese

if __name__ == '__main__':
    R, C = map(int, input().split())
    print(f1(R, C))
    print(f2(R, C))

