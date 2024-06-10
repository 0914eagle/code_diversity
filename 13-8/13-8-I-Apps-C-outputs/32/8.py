
import math

def area_covered(sandwich_radius, pickle_radius, num_pickles):
    # Calculate the area of the sandwich
    sandwich_area = math.pi * sandwich_radius ** 2
    
    # Calculate the area of a single pickle
    pickle_area = math.pi * pickle_radius ** 2
    
    # Calculate the total area covered by the pickles
    total_pickle_area = num_pickles * pickle_area
    
    # Calculate the percentage of the sandwich covered by the pickles
    covered_percentage = total_pickle_area / sandwich_area * 100
    
    return covered_percentage

def max_num_pickles(sandwich_radius, pickle_radius, max_coverage):
    # Initialize variables
    low = 0
    high = 7
    mid = (low + high) // 2
    
    # Binary search to find the maximum number of pickles that can be placed on the sandwich
    while low < high:
        if area_covered(sandwich_radius, pickle_radius, mid) <= max_coverage:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    
    return low

def main():
    sandwich_radius, pickle_radius, num_pickles, max_coverage = map(float, input().split())
    print(max_num_pickles(sandwich_radius, pickle_radius, max_coverage))

if __name__ == '__main__':
    main()

