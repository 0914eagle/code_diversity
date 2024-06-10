
import math

def get_input():
    return list(map(int, input().split()))

def get_pizza_area(radius, crust_width):
    return math.pi * radius ** 2 - math.pi * (radius - crust_width) ** 2

def get_cheese_area(pizza_area, crust_width):
    return pizza_area - math.pi * (radius - crust_width) ** 2

def get_cheese_percentage(pizza_area, crust_width):
    return get_cheese_area(pizza_area, crust_width) / pizza_area

def main():
    radius, crust_width = get_input()
    pizza_area = get_pizza_area(radius, crust_width)
    cheese_percentage = get_cheese_percentage(pizza_area, crust_width)
    print(cheese_percentage)

if __name__ == '__main__':
    main()

