
import math

def get_radius_and_crust(pizza):
    
    radius, crust = map(float, pizza.split())
    return radius, crust

def get_pizza_area(radius, crust):
    
    return math.pi * radius ** 2

def get_cheese_area(radius, crust, cheese_percentage):
    
    cheese_radius = radius - crust
    cheese_area = math.pi * cheese_radius ** 2 * cheese_percentage / 100
    return cheese_area

def get_cheese_percentage(radius, crust, cheese_area):
    
    pizza_area = get_pizza_area(radius, crust)
    return 100 * cheese_area / pizza_area

def main():
    pizza = input("Enter the pizza dimensions (radius and crust): ")
    radius, crust = get_radius_and_crust(pizza)
    cheese_area = get_cheese_area(radius, crust, 100)
    cheese_percentage = get_cheese_percentage(radius, crust, cheese_area)
    print(f"The percentage of cheese on the pizza is {cheese_percentage:.6f}%.")

if __name__ == '__main__':
    main()

