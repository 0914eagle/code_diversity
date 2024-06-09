
import math

def get_percentage_cheese(r, c):
    # Calculate the area of the crust
    area_crust = math.pi * c ** 2
    
    # Calculate the area of the pizza
    area_pizza = math.pi * r ** 2
    
    # Calculate the percentage of cheese
    percentage_cheese = 100 * (area_pizza - area_crust) / area_pizza
    
    return percentage_cheese

if __name__ == '__main__':
    r, c = map(int, input().split())
    print(get_percentage_cheese(r, c))

