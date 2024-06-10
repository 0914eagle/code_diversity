
import math

def get_input():
    return list(map(int, input().split()))

def get_cheese_percentage(r, c):
    area_crust = math.pi * c ** 2
    area_pizza = math.pi * r ** 2
    area_cheese = area_pizza - area_crust
    return area_cheese / area_pizza

def main():
    r, c = get_input()
    print(get_cheese_percentage(r, c))

if __name__ == '__main__':
    main()

