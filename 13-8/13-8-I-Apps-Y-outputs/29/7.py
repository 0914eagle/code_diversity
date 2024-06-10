
import math

def get_pizza_radius():
    return float(input())

def get_pizza_crust_width():
    return float(input())

def get_cheese_percentage(radius, crust_width):
    area_of_pizza = math.pi * radius ** 2
    area_of_crust = math.pi * (radius - crust_width) ** 2
    area_of_cheese = area_of_pizza - area_of_crust
    return area_of_cheese / area_of_pizza

def main():
    radius = get_pizza_radius()
    crust_width = get_pizza_crust_width()
    cheese_percentage = get_cheese_percentage(radius, crust_width)
    print(cheese_percentage)

if __name__ == '__main__':
    main()

