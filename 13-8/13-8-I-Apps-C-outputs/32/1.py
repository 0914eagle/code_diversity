
import math

def calculate_area_covered_by_pickles(n, r, s):
    # Calculate the area of a single pickle
    pickle_area = math.pi * r ** 2
    
    # Calculate the total area of all pickles
    total_pickle_area = n * pickle_area
    
    # Calculate the area of the sandwich
    sandwich_area = math.pi * s ** 2
    
    # Calculate the maximum area covered by pickles
    max_area_covered = sandwich_area * (100 - z) / 100
    
    # Return the number of pickles that can be placed on the sandwich
    return math.floor(max_area_covered / total_pickle_area)

def get_maximum_number_of_pickles(s, r, n, z):
    # Calculate the area covered by pickles
    area_covered_by_pickles = calculate_area_covered_by_pickles(n, r, s)
    
    # Calculate the maximum number of pickles that can be placed on the sandwich
    max_number_of_pickles = math.floor(area_covered_by_pickles / (math.pi * r ** 2))
    
    # Return the maximum number of pickles
    return max_number_of_pickles

def main():
    s, r, n, z = map(float, input().split())
    print(get_maximum_number_of_pickles(s, r, n, z))

if __name__ == '__main__':
    main()

