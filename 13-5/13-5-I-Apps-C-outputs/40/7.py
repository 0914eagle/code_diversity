
def get_distinct_starting_circles(circle, k):
    # Initialize a set to store the distinct starting circles
    distinct_circles = set()
    
    # Iterate over the possible starting circles
    for i in range(len(circle)):
        # Get the starting circle by rotating the input circle by i positions
        starting_circle = circle[i:] + circle[:i]
        
        # Initialize a set to store the distinct transformed circles
        transformed_circles = set()
        
        # Iterate over the possible transformations
        for j in range(k):
            # Get the transformed circle by inserting a black pebble between two neighbouring pebbles of the same color, and a white pebble between two neighbouring pebbles of different colors
            transformed_circle = ""
            for i in range(len(starting_circle) - 1):
                if starting_circle[i] == starting_circle[i + 1]:
                    transformed_circle += "B"
                else:
                    transformed_circle += "W"
            transformed_circle += starting_circle[-1]
            
            # Add the transformed circle to the set of distinct transformed circles
            transformed_circles.add(transformed_circle)
        
        # If the set of distinct transformed circles is equal to the set of distinct starting circles, add the starting circle to the set of distinct starting circles
        if transformed_circles == distinct_circles:
            distinct_circles.add(starting_circle)
    
    # Return the number of distinct starting circles
    return len(distinct_circles)

def main():
    # Read the input
    n, k = map(int, input().split())
    circle = input()
    
    # Call the function to get the number of distinct starting circles
    result = get_distinct_starting_circles(circle, k)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

