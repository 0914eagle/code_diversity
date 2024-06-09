
import math

def get_regions(circles):
    # Initialize a set to store the regions
    regions = set()
    
    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle
        
        # Calculate the area of the circle
        area = math.pi * r ** 2
        
        # Add the area to the set of regions
        regions.add(area)
    
    # Return the number of regions
    return len(regions)

def main():
    # Read the number of circles from stdin
    n = int(input())
    
    # Read the circles from stdin
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    
    # Call the get_regions function and print the result
    print(get_regions(circles))

if __name__ == '__main__':
    main()

