
import math

def get_pizza_info():
    r, c = map(int, input().split())
    return r, c

def get_cheese_percentage(r, c):
    area_crust = math.pi * (r ** 2) * (c / 100)
    area_cheese = math.pi * (r ** 2) - area_crust
    return area_cheese / (math.pi * (r ** 2))

def main():
    r, c = get_pizza_info()
    print(get_cheese_percentage(r, c))

if __name__ == '__main__':
    main()

