
import math

def get_regions(circles):
    # Initialize a set to store the regions
    regions = set()
    
    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle
        
        # Get the bounding box of the circle
        left = x - r
        right = x + r
        top = y + r
        bottom = y - r
        
        # Get the four corners of the bounding box
        top_left = (left, top)
        top_right = (right, top)
        bottom_left = (left, bottom)
        bottom_right = (right, bottom)
        
        # Add the four corners to the set of regions
        regions.add(top_left)
        regions.add(top_right)
        regions.add(bottom_left)
        regions.add(bottom_right)
    
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

