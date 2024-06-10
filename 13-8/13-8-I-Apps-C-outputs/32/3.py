
import math

def get_max_pickles(s, r, n, z):
    # Calculate the area of the sandwich
    area_sandwich = math.pi * s ** 2
    
    # Calculate the area of a single pickle
    area_pickle = math.pi * r ** 2
    
    # Calculate the maximum area that can be covered by pickles
    max_area_covered = area_sandwich * z / 100
    
    # Calculate the maximum number of pickles that can be placed on the sandwich
    max_pickles = math.floor(max_area_covered / area_pickle)
    
    return max_pickles

def main():
    s, r, n, z = map(float, input().split())
    print(get_max_pickles(s, r, n, z))

if __name__ == '__main__':
    main()

