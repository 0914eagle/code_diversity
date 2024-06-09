
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
        corners = [(left, top), (right, top), (right, bottom), (left, bottom)]
        
        # Iterate over the corners and check if they are inside the circle
        for corner in corners:
            # Get the distance between the corner and the center of the circle
            distance = math.sqrt((corner[0] - x) ** 2 + (corner[1] - y) ** 2)
            
            # If the distance is less than or equal to the radius, the corner is inside the circle
            if distance <= r:
                # Add the corner to the region
                regions.add(corner)
    
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

