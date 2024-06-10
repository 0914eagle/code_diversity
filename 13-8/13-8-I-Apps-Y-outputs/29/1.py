
import math

def get_percentage(r, c):
    # Calculate the area of the crust
    crust_area = math.pi * c ** 2
    
    # Calculate the area of the cheese
    cheese_area = math.pi * (r ** 2 - c ** 2)
    
    # Calculate the percentage of cheese
    percentage = cheese_area / (crust_area + cheese_area)
    
    return percentage

def main():
    r, c = map(int, input().split())
    print(get_percentage(r, c))

if __name__ == '__main__':
    main()

