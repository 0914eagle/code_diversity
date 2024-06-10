
import math

def get_maximum_pickles(sandwich_radius, pickle_radius, number_of_pickles, max_area):
    # Calculate the area of the sandwich
    sandwich_area = math.pi * sandwich_radius ** 2
    
    # Calculate the area of a single pickle
    pickle_area = math.pi * pickle_radius ** 2
    
    # Calculate the maximum number of pickles that can be placed on the sandwich
    max_pickles = sandwich_area // pickle_area
    
    # Calculate the maximum area that can be covered by the pickles
    max_coverage = max_pickles * pickle_area
    
    # Return the maximum number of pickles that can be placed on the sandwich while staying within the given constraints
    return min(max_pickles, math.ceil(max_coverage * (max_area / 100)))

def main():
    sandwich_radius, pickle_radius, number_of_pickles, max_area = map(float, input().split())
    print(get_maximum_pickles(sandwich_radius, pickle_radius, number_of_pickles, max_area))

if __name__ == '__main__':
    main()

